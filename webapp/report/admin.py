from django.contrib import admin

from .models import PotholeReport
from .models.image import PotholeImage

admin.site.register(PotholeReport)
admin.site.register(PotholeImage)
