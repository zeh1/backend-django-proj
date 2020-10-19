from django.contrib import admin

# Register your models here.

from .models import Users, Posts, Replies

admin.site.register(Users)
admin.site.register(Posts)
admin.site.register(Replies)