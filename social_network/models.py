from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="posts/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
    )

    def __str__(self):
        return f"{self.title} by {self.user}"


class UserFollowing(models.Model):
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="following",
    )
    following_user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="followers",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("user_id", "following_user_id"),)
        indexes = [
            models.Index(fields=["user_id", "following_user_id"]),
        ]
        ordering = ("created_at",)

    def clean(self):
        if self.user_id == self.following_user_id:
            raise ValidationError("You can't follow yourself")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user_id} follows {self.following_user_id}"
