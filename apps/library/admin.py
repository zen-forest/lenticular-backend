from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("url", "user", "created_at")  
    search_fields = ("url",)
    list_filter = ("created_at",) 
