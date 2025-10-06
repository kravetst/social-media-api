from django.contrib import admin

from social_network.models import Post, UserFollowing

admin.site.register(Post)
admin.site.register(UserFollowing)
