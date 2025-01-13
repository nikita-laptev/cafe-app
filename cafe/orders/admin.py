from django.contrib import admin
from .models import Status, CookingStatus, Order, OrderItem

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('status_name',)
    search_fields = ('status_name',)
    ordering = ('status_name',)
    list_filter = ('status_name',)

@admin.register(CookingStatus)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('cooking_status_name',)
    search_fields = ('cooking_status_name',)
    ordering = ('cooking_status_name',)
    list_filter = ('cooking_status_name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('date', 'waiter', 'status', 'cooking_status',)
    ordering = ('date',)
    list_filter = ('date', 'waiter', 'status', 'cooking_status',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'dish', 'quantity',)
    ordering = ('quantity',)
    list_filter = ('quantity',)
