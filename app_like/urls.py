from django.urls import path
from .views import liked, unliked


app_name = "app_like"
urlpatterns = [
    path('liked/<pk>/', liked, name='liked_post'),
    path('unliked/<pk>/', unliked, name='unliked_post'),
]
