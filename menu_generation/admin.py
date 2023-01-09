from django.contrib import admin

from .models import Menu, MenuItem


class MenuAdmin(admin.ModelAdmin):
    model = Menu
    list_display = ["name", "status"]
    list_display_links = ["name"]
    ordering = ["name"]


class MenuItemAdmin(admin.ModelAdmin):
    model = MenuAdmin
    list_display = ["menu", "parent", "name", "status"]
    list_display_links = ["name"]
    list_filter = ["menu", "status"]
    ordering = ["name"]


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
