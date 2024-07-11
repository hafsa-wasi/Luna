from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('home/' , views.index, name='index'),
    path('<str:sign>/post/' , views.post_view, name='post'),
    path('get/<str:sign>/<str:id>/' , views.get_view, name='get'),
    path('get/<str:sign>/<str:id>/edit/' , views.edit_view, name='edit'),
    path('get/<str:sign>/<str:id>/delete/' , views.delete_view, name='delete'),
    path('<str:sign>/recent/' , views.recent_more, name='recent'),
    path('<str:id>/like/' , views.liked_post_view, name='like'),
    path('<str:id>/<str:sign>/summarize/', views.chatbot_view, name='summarize'),
    path('<str:sign>/search/' , views.search_view, name='search'),
    path('<str:sign>/<str:tag>/' , views.tags_view, name='tags'),
]