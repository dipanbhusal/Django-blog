from django.urls import path 
from .views import home, postDetail, PostCreate,postUpdate, postDelete

app_name ='blog'
urlpatterns = [
    path('', home, name ='home' ),
    path('create/', PostCreate, name ='create' ),
    path('post/<slug:post_slug>', postDetail, name ='post-detail'),
    path('post/<slug:post_slug>/update/', postUpdate, name ='post-update'),
    path('post/<slug:post_slug>/delete/', postDelete, name ='post-delete'),
] 