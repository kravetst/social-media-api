from rest_framework import serializers
from social_network.models import Post, UserFollowing


class PostSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(
        source="user.email", read_only=True
    )
    class Meta:
        model = Post
        fields = ("id", "title", "description", "user_email")


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "description")


class PostDetailSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(
        source="user.email", read_only=True
    )
    user_first_name = serializers.CharField(
        source="user.first_name", read_only=True
    )
    user_last_name = serializers.CharField(
        source="user.last_name", read_only=True
    )

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "description",
            "image",
            "user_email",
            "user_first_name",
            "user_last_name",
            "created_at",
            "updated_at",
        )


class UserFollowingSerializer(serializers.ModelSerializer):
    following_user_email = serializers.EmailField(
        source="following_user_id.email", read_only=True
    )

    class Meta:
        model = UserFollowing
        fields = (
            "id", "following_user_id", "created_at", "following_user_email"
        )


class UserFollowerSerializer(serializers.ModelSerializer):
    followers_user_email = serializers.EmailField(
        source="user_id.email", read_only=True
    )

    class Meta:
        model = UserFollowing
        fields = ("id", "user_id", "created_at", "followers_user_email")
