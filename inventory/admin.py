from django.contrib import admin

from .models import Platform, Game


class GameAdmin(admin.ModelAdmin):
    fields = ['game_name', 'hours_played', 'platform']
    list_display = ('game_name', 'hours_played', 'platform')
    list_editable = ['hours_played']
    list_filter = ['platform']
    search_fields = ['game_name']


class PlatformAdmin(admin.ModelAdmin):
    fields = ['platform_name', 'family', 'generation', 'release_date']
    list_display = ('platform_name', 'family', 'generation', 'release_date', 'is_current_generation')
    list_editable = ['family', 'generation']
    list_filter = ['family']
    search_fields = ['platform_name']


admin.site.register(Platform, PlatformAdmin)
admin.site.register(Game, GameAdmin)
