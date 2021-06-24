from django.contrib import admin
from .models import Code


class CodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'discount', 'active']

admin.site.register(Code, CodeAdmin)
