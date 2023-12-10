from django.db import models
from django.contrib.auth.models import User


class PostQuerySet(models.QuerySet):
    def public_posts(self):
        return self.filter(is_public=True).order_by("-created_at")


class Post(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)

    objects = PostQuerySet.as_manager()

    def __str__(self):
        return f"Post by {self.posted_by.username} at {self.created_at}"
