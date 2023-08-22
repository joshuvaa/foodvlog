from django.contrib import admin
from .models import *


# Register your models here.

class categadmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(categ, categadmin)


class prodadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug', 'price', 'stock','img']
    list_editable = ['price','stock','img']


admin.site.register(Products, prodadmin)
