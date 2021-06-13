from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from .forms import ProfilePic, SignUpForm, UserProfileChange
from django.contrib.auth.decorators import login_required

# Create your views here.


def sign_up_view(request):
    form = SignUpForm()
    registered = False
    if request.method == "POST":
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
    dict = {
        "form": form,
        "registered": registered,
    }
    return render(request, "app_auth/signup.html", context=dict)


def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('app_post:post_list'))
    return render(request, 'app_auth/login.html', context={'form': form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('app_post:post_list'))


@login_required
def profile(request):
    return render(request, 'app_auth/profile.html', context={})


@login_required
def user_change(request):
    current_user = request.user
    form = UserProfileChange(instance=current_user)
    if request.method == 'POST':
        form = UserProfileChange(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChange(instance=current_user)
    return render(request, 'app_auth/change_profile.html', context={'form': form})


@login_required
def pass_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            changed = True
    return render(request, 'app_auth/pass_change.html', context={'form': form, 'changed': changed})



@login_required
def change_pro_pic(request):
    form = ProfilePic(instance=request.user.user_profile)
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES,
                          instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app_auth:profile'))
    return render(request, 'app_auth/pro_pic_add.html', context={'form': form})
