from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from app_like.models import Like
from app_post.models import Post
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


@login_required
def liked(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(post=post, user=user)
    if not already_liked:
        liked_post = Like(post=post, user=user)
        liked_post.save()
    return HttpResponseRedirect(reverse('app_post:post_details', kwargs={'slug': post.slug}))


@login_required
def unliked(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(post=post, user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('app_post:post_details', kwargs={'slug': post.slug}))
