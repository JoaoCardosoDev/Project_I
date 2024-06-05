from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from filemanager.forms import FolderForm

# Create your views here.

# view to see all the current folders
def landing():
    return

#view inside the folder
def folder_screen():
    return

def create_folder(request):
    if request.method == 'POST':
        form = FolderForm(request.POST)
        print(form)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.save()
            return HttpResponseRedirect(reverse('index'))


    context = {'form': FolderForm()}
    return render(request, 'filemanager/index.html', context)

def root(request):
    return render(request, 'filemanager/index.html')