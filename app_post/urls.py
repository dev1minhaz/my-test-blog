from .views import CreatePost, MyPosts, UpdatePost, post_details, PostList
from django.urls import path

app_name="app_post"

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('details/<slug:slug>', post_details, name='post_details'),
    path('write/', CreatePost.as_view(), name='create_post'),
    path('my-blogs/', MyPosts.as_view(), name='my_blogs'),
    path('edit/<pk>/', UpdatePost.as_view(), name='edit_blog'),
]
