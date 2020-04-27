from django.urls import path 
from .views import (
    PostListApiView,
    PostDetailApiVIew,
    PostDeleteApiVIew,
    PostUpdateApiVIew,
    PostCreateApiView
)
app_name = 'blog' 
urlpatterns = [
    
    path('', PostListApiView.as_view(),  name='list'),
    path('create', PostCreateApiView.as_view(),  name='create'),
    path('<slug:post_slug>', PostDetailApiVIew.as_view(),  name='detail'),
    path('<slug:post_slug>/delete', PostDeleteApiVIew.as_view(),  name='delete'),
    path('<slug:post_slug>/update', PostUpdateApiVIew.as_view(),  name='update'),
]