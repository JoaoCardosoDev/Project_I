from django import forms
from filemanager.models import Folder, File

class FolderForm(forms.ModelForm):
    create_folder = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Folder
        fields = ('title',)

class FileForm(forms.ModelForm):
    create_file = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = File
        fields = ('title', 'storage')
