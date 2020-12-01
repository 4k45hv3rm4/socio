from django.contrib import admin
from .models import User, FriendRequest, Post


admin.site.register(User)
admin.site.register(FriendRequest)
admin.site.register(Post)