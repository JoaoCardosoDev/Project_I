from django.contrib import admin

from EticDrive.models import NormalUser
from filemanager.models import File, Folder

# Register your models here.

@admin.register(NormalUser)
class UserAdmin(admin.ModelAdmin):
    pass
