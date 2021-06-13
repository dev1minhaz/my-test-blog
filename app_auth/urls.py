from django.urls import path
from .views import change_pro_pic, login_page, logout_user, pass_change, profile, sign_up_view, user_change

app_name = "app_auth"

urlpatterns = [
    path('signup/', sign_up_view, name="signup"),
    path('login/', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
    path('change-profile/', user_change, name='user_change'),
    path('password/', pass_change, name='pass_change'),
    path('add-picture/', change_pro_pic, name='add_pro_pic'),
    path('change-picture/', change_pro_pic, name='change_pro_pic'),
]
