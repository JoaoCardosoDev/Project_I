from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from filemanager.forms import FolderForm, FileForm
from filemanager.models import File, Folder

# Create your views here.

def root(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    return render(request, 'filemanager/index.html')

def home(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            print("method post")
            form = FolderForm(request.POST)
            if form.is_valid():
                print("form valid")
                folder = form.save()
                folder.user = request.user
                folder.path = "default"
                folder.save()
                return HttpResponseRedirect(reverse('home'))
        
        folders = Folder.objects.filter(user=request.user)
        files = File.objects.filter(user=request.user)
        form = FolderForm()
        fileform = FileForm()

        context = {
            'form': form,
            'fileform': fileform,
            'folders': folders,
            'files': files
        }
        return render(request, 'filemanager/home.html', context)
        

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
