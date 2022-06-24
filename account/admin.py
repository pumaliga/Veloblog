from django.contrib import admin

from account.models import CustomUser, Post


admin.site.register(CustomUser)
admin.site.register(Post)
