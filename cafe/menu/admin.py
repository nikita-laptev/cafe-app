from django.contrib import admin
from .models import Category, Menu

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name',)
    ordering = ('name',)
    list_filter = ('name',)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category',)
    search_fields = ('name',)
    ordering = ('name', 'price',)
    list_filter = ('name', 'category')