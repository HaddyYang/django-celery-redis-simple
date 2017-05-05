#coding:utf-8
from django.contrib import admin
from .models import Blog

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """blog admin"""
    list_display=('id', 'caption')
