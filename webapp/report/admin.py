from django.contrib import admin

from .models import PotholeImage, PotholeReport

admin.register.site(PotholeReport)
admin.register.site(PotholeImage)
