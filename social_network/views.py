from rest_framework import viewsets, mixins, permissions
from social_network.models import Post, UserFollowing
from social_network.serializers import (
    PostSerializer,
    PostCreateSerializer,
    PostDetailSerializer,
    UserFollowingSerializer,
    UserFollowerSerializer
)


class OwnPostViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin
):
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):

        if self.action == "create":
            return PostCreateSerializer
        if self.action == "retrieve":
            return PostDetailSerializer
        return PostSerializer

    def get_queryset(self):
        return Post.objects.select_related("user").filter(user=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FollowingPostViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PostDetailSerializer
        return PostSerializer

    def get_queryset(self):
        following_user_ids = list(
            UserFollowing
            .objects
            .filter(user_id__id=self.request.user.id)
            .select_related("user_id", "following_user_id")
            .values_list("following_user_id", flat=True)
        )

        return self.queryset.filter(user__in=following_user_ids).select_related("user")


class UserFollowingViewSet(viewsets.ModelViewSet):
    serializer_class = UserFollowingSerializer
    queryset = UserFollowing.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return (
            UserFollowing
            .objects.
            select_related("user_id", "following_user_id")
            .filter(user_id__id=self.request.user.id)
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserFollowerViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    serializer_class = UserFollowerSerializer
    queryset = UserFollowing.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return (
            UserFollowing.objects.select_related("user_id", "following_user_id")
            .exclude(user_id__id=self.request.user.id)
            .filter(following_user_id__id=self.request.user.id)
        )
