from django.contrib import admin

from _user.models import User, UserProfile

admin.site.register(User)
admin.site.register(UserProfile)
