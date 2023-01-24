from django.contrib import admin
from .models import FillerTextModel


class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'original')
    list_display_links = ('id', 'title')


# Register your models here.
admin.site.register(FillerTextModel, TableAdmin)
