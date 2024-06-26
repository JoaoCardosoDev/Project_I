from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings
import mimetypes
import os

# Create your models here.
class Base(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lastmodified = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        lastmodified = models.DateTimeField(auto_now_add=True)
        super().save(*args, **kwargs)

class Folder(Base):
    parent = models.ForeignKey('Folder', on_delete=models.CASCADE, related_name='folder_children', null=True, blank=True)
    favorite = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.title}"

class File(Base):
    parent = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, blank=True)
    storage = models.FileField()

    def save(self, *args, **kwargs):
        file_obj = self.storage
        file_name, file_extension = os.path.splitext(file_obj.name)
        file_type, _ = mimetypes.guess_type(file_obj.name)
        if file_type:
            file_type = file_type.split('/')[-1]
        else:
            file_type = ''

        self.storage.name = f"{self.title}.{file_type}"
        super().save(*args, **kwargs)
    
#Delete file when its model is deleted

from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.db import models
 

""" Whenever ANY model is deleted, if it has a file field on it, delete the associated file too"""
@receiver(post_delete)
def delete_files_when_row_deleted_from_db(sender, instance, **kwargs):
    for field in sender._meta.concrete_fields:
        if isinstance(field,models.FileField):
            instance_file_field = getattr(instance,field.name)
            delete_file_if_unused(sender,instance,field,instance_file_field)
            
""" Delete the file if something else get uploaded in its place"""
@receiver(pre_save)
def delete_files_when_file_changed(sender,instance, **kwargs):
    if not instance.pk:
        return
    for field in sender._meta.concrete_fields:
        if isinstance(field,models.FileField):
            try:
                instance_in_db = sender.objects.get(pk=instance.pk)
            except sender.DoesNotExist:
                return
            instance_in_db_file_field = getattr(instance_in_db,field.name)
            instance_file_field = getattr(instance,field.name)
            if instance_in_db_file_field.name != instance_file_field.name:
                delete_file_if_unused(sender,instance,field,instance_in_db_file_field)

""" Only delete the file if no other instances of that model are using it"""    
def delete_file_if_unused(model,instance,field,instance_file_field):
    dynamic_field = {}
    dynamic_field[field.name] = instance_file_field.name
    other_refs_exist = model.objects.filter(**dynamic_field).exclude(pk=instance.pk).exists()
    if not other_refs_exist:
        instance_file_field.delete(False)