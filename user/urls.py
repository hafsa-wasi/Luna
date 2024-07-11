from django.urls import path
from . import views

#from django.contrib import admin

urlpatterns = [
    path('signin/' , views.signin ,name='signin'),
    path('user_home/' , views.user_home , name='user_home'),
    path('signup/' , views.register.as_view() ,name='signup'),
    path('signout/', views.logout_view , name = 'signout'),
    path('user_profile/' , views.user_profile , name='profile'),
    path('update_profile/' , views.update_profile , name='update'),
    path('delete_profile/' , views.delete_profile , name='delete'),

    ]