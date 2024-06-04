from django.shortcuts import render

from filemanager.forms import FolderForm

# Create your views here.

# view to see all the current folders
def landing():
    return

#view inside the folder
def folder_screen():
    return

def create_folder(request):
    context = {'form': FolderForm()}
    return render(request, 'EticDrive/index.html', context)

def root(request):
    return render(request, 'EticDrive/index.html')