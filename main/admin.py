from django.contrib import admin
from . import models

class AdminSection(admin.ModelAdmin):
  list_display = ('title', 'date')
  list_display_links = ('title',)
  search_fields = ('title', 'date')

admin.site.register(models.Section, AdminSection)


class AdminTheme(admin.ModelAdmin):
  list_display = ('title', 'section', 'user', 'date')
  list_display_links = ('title',)
  search_fields = ('title', 'section', 'user', 'date')
  
admin.site.register(models.Theme, AdminTheme)

class AdminMessage(admin.ModelAdmin):
  list_display = ('text', 'theme', 'user', 'date')
  list_display_links = ('text', 'theme', 'user')
  search_fields = ('text', 'theme', 'user', 'date')

admin.site.register(models.Message)
