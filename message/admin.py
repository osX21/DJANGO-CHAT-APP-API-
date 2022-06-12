from django.contrib import admin
from .models import *

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'get_date')
    