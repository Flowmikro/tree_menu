from django.contrib import admin

from .models import MenuModel


@admin.register(MenuModel)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'named_url', 'parent')
    prepopulated_fields = {'named_url': ('name',)}