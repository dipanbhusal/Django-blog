from django.urls import path 
from .views import commentThread, comment_delete
app_name ='comments'
urlpatterns = [
   
    path('<int:id>', commentThread, name ='comment-thread'),
    path('<int:id>/delete/', comment_delete, name ='comment-delete'),
    #path('post/<slug:post_slug>/delete/', postDelete, name ='post-delete'),
]  