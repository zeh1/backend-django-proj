from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length = 16, unique = True)
    email = models.TextField(max_length = 320, unique = True)
    password = models.CharField(max_length = 100)
    joined = models.DateTimeField(auto_now_add = True)
    post_count = models.IntegerField(null = True)

class Posts(models.Model):
    title = models.TextField(max_length = 250, null = False)
    body = models.TextField(max_length = 500, null = False)
    date = models.DateTimeField(auto_now_add = True)
    user_id = models.ForeignKey('Users', on_delete = models.CASCADE)
    upvotes = models.IntegerField(null = True)
    downvotes = models.IntegerField(null = True)

class Replies(models.Model):
    body = models.TextField(max_length = 500, null = False)
    user_id = models.ForeignKey('Users', on_delete = models.CASCADE)
    post_id = models.ForeignKey('Posts', on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)

