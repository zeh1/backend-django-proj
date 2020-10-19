from django.db import models

# Create your models here.


class Users(model.Model):
    username = models.CharField(max_length = 16, unique = True)
    email = models.TextField(max_length = 320, unique = True)
    password = models.CharField(max_length = 100)
    joined = models.DateTimeField(auto_now_add = True)
    posts = models.IntegerField(null = True)

class Posts(model.Model):
    title = models.TextField(max_length = 250, null = False)
    body = models.TextField(max_length = 500, null = False)
    date = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey('Users')
    upvotes = models.IntegerField(null = True)
    downvotes = models.IntegerField(null = True)

class Replies(model.Model):
    body = models.TextField(max_length = 500, null = False)
    user = models.ForeignKey('Users')
    post = models.ForeignKey('Posts')
    date = models.DateTimeField(auto_now_add = True)

