from .permissions import LoginRequiredandAuthorMixin
from django.views.generic.edit import UpdateView
from app_like.models import Like
from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView
from .models import Post
from django.contrib.auth.decorators import login_required
from app_comment.forms import CommentForm
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse, reverse_lazy
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
import uuid
from slugify import slugify

# Create your views here.


class PostList(ListView):
    context_object_name = 'posts'
    model = Post
    paginate_by = 8
    template_name = 'app_post/post_list.html'


@login_required
def post_details(request, slug):
    post = Post.objects.get(slug=slug)
    comment_form = CommentForm()
    already_liked = Like.objects.filter(post=post, user=request.user)
    if already_liked:
        liked = True
    else:
        liked = False
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('app_post:post_details', kwargs={'slug': slug}))
    return render(request, 'app_post/post_details.html', context={'post': post, 'comment_form': comment_form, 'liked': liked, })


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'app_post/create_post.html'
    fields = ('blog_title', 'blog_content', 'blog_image',)

    def form_valid(self, form):
        post_object = form.save(commit=False)
        post_object.author = self.request.user
        title = post_object.blog_title
        post_object.slug = slugify(title+str(uuid.uuid4()))
        post_object.save()
        return HttpResponseRedirect(reverse('app_post:post_list'))


class MyPosts(LoginRequiredMixin, TemplateView):
    template_name = 'app_post/my_posts.html'


class UpdatePost(LoginRequiredandAuthorMixin, UpdateView):
    model = Post
    fields = ('blog_title', 'blog_content', 'blog_image')
    template_name = 'app_post/edit_post.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('app_post:post_details', kwargs={'slug': self.object.slug})
