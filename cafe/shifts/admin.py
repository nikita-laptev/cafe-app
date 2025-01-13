from django.contrib import admin
from .models import Shift, ShiftUser

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('date', 'start_time', 'end_time',)
    list_filter = ('date',)

@admin.register(ShiftUser)
class ShiftUserAdmin(admin.ModelAdmin):
    list_display = ('shift', 'user')
