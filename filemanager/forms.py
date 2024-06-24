from django import forms
from filemanager.models import Base, Folder, File

class FolderForm(forms.ModelForm):
    create_folder = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Folder
        fields = ('title', 'parent', 'favorite')

class FileForm(forms.ModelForm):
    create_file = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = File
        fields = ('title', 'storage')

class SearchForm(forms.ModelForm):
    model=Base
    search = forms.BooleanField(widget=forms.HiddenInput, initial=True)