from django.db import models
from app_post.models import Post
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Like(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="liked_blog")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="liker_user")

    def __str__(self):
        return f"{self.user} likes {self.post}"
