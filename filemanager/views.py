from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from filemanager.forms import FolderForm, FileForm
from filemanager.models import File, Folder

# Create your views here.

def root(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    return render(request, 'filemanager/index.html')

@login_required(login_url="/login")
def home(request):
    folder_form = FolderForm()
    file_form = FileForm()

    if request.method == 'POST':
        if 'create_folder' in request.POST:
            form = FolderForm(request.POST)
            if form.is_valid():
                folder = form.save(commit=False)  
                folder.user = request.user  
                folder.save()  
                return HttpResponseRedirect(reverse('home'))
        if 'create_file' in request.POST:
            form = FileForm(request.POST, request.FILES)
            if form.is_valid():
                file = form.save(commit=False)  
                file.user = request.user  
                file.save()  
                return HttpResponseRedirect(reverse('home'))
            # else:
            #     print(form.errors)  # Print errors for debugging
            #     folder_form = FolderForm()
            #     file_form = form  # Reassign the form with errors

    folders = Folder.objects.filter(user=request.user)
    files = File.objects.filter(user=request.user)

    context = {
        'form': folder_form,
        'fileform': file_form,
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
