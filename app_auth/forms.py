from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import UserProfile


User = get_user_model()


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email Address", required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')


class ProfilePic(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_picture',)
