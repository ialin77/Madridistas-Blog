from django.urls import path
from .views import (
    UserPostListView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,

)
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:str>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='create-post'),
    path('post/<int:pk>/', PostUpdateView.as_view(), name='update-post'),
    path('post/<int:pk>/', PostDeleteView.as_view(), name='delete-post'),
    path('about/', views.about, name='about'),


]