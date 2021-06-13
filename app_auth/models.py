from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.


def user_img_path(instance, filename):
    return f'profile_pictures/{instance.user}/{filename}'


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_profile")
    profile_picture = models.ImageField(
        upload_to=user_img_path, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}"


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.user_profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
