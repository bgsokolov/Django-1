from django.contrib import admin

# Register your models here.
from .models import Mode

# Register the Mode model in admin (no class)
# admin.site.register(Mode)

# Define the admin class
class ModeAdmin(admin.ModelAdmin):
    pass
# Define list of columns displayed in admin panel
class ModeAdmin(admin.ModelAdmin):
    list_display = ('mode_name', 'mode_desc')

# Register the admin class with the associated model
admin.site.register(Mode, ModeAdmin)

