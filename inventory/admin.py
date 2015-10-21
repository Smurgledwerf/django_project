from django.contrib import admin

from .models import Platform, Game


class GameInLine(admin.TabularInline):
    model = Game
    extra = 2


class PlatformAdmin(admin.ModelAdmin):
    fields = ['platform_name', 'release_date']
    inlines = [GameInLine]
    list_display = ('platform_name', 'release_date')
    search_fields = ['platform_name']


admin.site.register(Platform, PlatformAdmin)
