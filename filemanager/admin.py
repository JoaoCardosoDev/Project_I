from django.contrib import admin

from filemanager.models import File, Folder

# Register your models here.

@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    pass

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    pass
