from django.contrib import admin
from django import forms
from .models import Picture

from .models import Picture, Like, Comment

# Register your models here.


class PictureAdmin(admin.ModelAdmin):

    model = Picture
    fields = ('name', 'image', 'author')
    list_display = ('name', 'image', 'author')


admin.site.register(Picture, PictureAdmin)
admin.site.register(Like)
admin.site.register(Comment)
