from django.db import models
from app_post.models import Post
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='blog_comment')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-comment_date',)

    def __str__(self):
        return f"{self.user}==={self.post}=={(self.comment)[:25]}"
