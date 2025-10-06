from rest_framework import routers
from social_network.views import (
    OwnPostViewSet,
    UserFollowingViewSet,
    UserFollowerViewSet,
    FollowingPostViewSet
)

router = routers.DefaultRouter()
router.register("own_posts", OwnPostViewSet, basename="own_posts")
router.register(
    "following_posts",
    FollowingPostViewSet,
    basename="following_posts"
)
router.register("followings", UserFollowingViewSet)
router.register("followers", UserFollowerViewSet, basename="followers")

urlpatterns = router.urls

app_name = "social_network"
