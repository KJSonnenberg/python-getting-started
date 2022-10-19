from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','created')
    list_filter = ['created', 'updated']
    list_per_page = 25
    ordering = ('-created', 'updated')
    search_fields = ('title', 'description')
    
admin.site.register(Item, ItemAdmin)
