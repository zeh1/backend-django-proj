from django.urls import path

from . import views

urlpatterns = [
    path('posts', views.posts, name='posts'),
    path('posts/<int:post_id>', views.post, name="post"),
    path('posts/<int:post_id>/replies', views.replies, name='replies'),
    path('posts/<int:post_id>/replies/<int:reply_id>', views.reply, name="reply")
]