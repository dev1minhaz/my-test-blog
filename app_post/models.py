from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post_author')
    blog_title = models.CharField(max_length=264, verbose_name="Put a Title")
    slug = models.SlugField(max_length=264, unique=True)
    blog_content = models.TextField(verbose_name="What is on your mind?")
    blog_image = models.ImageField(
        upload_to='blog_images', verbose_name="Image")
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date', ]

    def __str__(self):
        return f"{self.author} {self.blog_title}"
