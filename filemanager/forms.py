from django import forms
from filemanager.models import Folder

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ('title',)

