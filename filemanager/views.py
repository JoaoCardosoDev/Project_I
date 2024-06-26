from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from filemanager.forms import FolderForm, FileForm
from filemanager.models import Base, File, Folder
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib import messages
# Create your views here.

def root(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    return render(request, 'filemanager/root.html')

@login_required(login_url="/login")
def home(request):
    if request.user.is_staff:
        return redirect('admin:index')
    
    breadcrumb = "Workspace"
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

            file_obj = request.FILES['storage']
            
            if file_obj.size < (request.user.max_quota - request.user.quota_counter):

                # messages.error(request, "File size exceeds 1MB")
                folder_form = FolderForm()
                file_form = FileForm()
            else:
                form = FileForm(request.POST, request.FILES)
                if form.is_valid():
                    file = form.save(commit=False)  
                    file.user = request.user  
                    file.save()
                    request.user.quota_counter += file_obj.size
                    request.user.save()
                    return HttpResponseRedirect(reverse('home'))
                else:
                    folder_form = FolderForm()
                    file_form = form

        if 'search_query' in request.POST:
            search_query = request.POST.get('search_query')
            search_result = Base.objects.filter(user=request.user, title__contains=search_query)
            folders = search_result
            files = ""
            breadcrumb = f"Search result: {search_query}"
        
        else:
            messages.error(request, "No file uploaded")
            folder_form = FolderForm()
            file_form = FileForm()
    
    folders = Folder.objects.filter(user=request.user, parent = None)
    files = File.objects.filter(user=request.user)
    favfolders = Folder.objects.filter(user=request.user, favorite=True)
    lastmod = Base.objects.filter(user=request.user).order_by('-lastmodified')
    quota_mb = format(request.user.quota_counter / (1024 * 1024), '.2f')

    context = {
        'form': folder_form,
        'fileform': file_form,
        'folders': folders,
        'files': files,
        'favfolders': favfolders,
        'Lastmod': lastmod,
        'breadcrumb': breadcrumb,
        'quota': quota_mb
    }
    return render(request, 'filemanager/home.html', context)


@login_required(login_url="/login")
def deleteInstance(request, id=None):
    instance = get_object_or_404(Base, pk=id)
    if request.user == instance.user:
        request.user.quota_counter -= instance.file.size
        request.user.save()
        instance.delete()
    return HttpResponseRedirect(reverse('home'))

@login_required(login_url="/login")
def editInstance(request, id=None):
    instance = get_object_or_404(Base, pk=id)
    if request.user == instance.user:
        for model in [Folder, File]:
            try:
                instance = model.objects.get(pk=id)
                break
            except model.DoesNotExist:
                pass
        else:
            raise Http404

        form_class = FolderForm if isinstance(instance, Folder) else FileForm

        if request.method == 'POST':
            form = form_class(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('home'))
        else:
            form = form_class(instance=instance)

    return render(request, 'filemanager/edit.html', {'form': form})


@login_required(login_url="/login")
def download(request, id=None):
    file = File.objects.get(pk=id)
    storage = FileSystemStorage()
    path = storage.path(file.title)
    response = FileResponse(open(path, 'rb'), as_attachment=True, filename=file.title)
    response['Content-Disposition'] = f'attachment; filename="{file.title}"'
    return response

@login_required(login_url="/login")
def folderView(request, id=None):

    if request.user.is_staff:
        return redirect('admin:index')
    
    folder = get_object_or_404(Folder, pk=id)
    folderChildren = Folder.objects.filter(parent=folder)
    files = File.objects.filter(parent=folder)
    folder_form = FolderForm()
    file_form = FileForm()
    favfolders = Folder.objects.filter(user=request.user, favorite=True)
    
    def get_breadcrumb(request, folder):
        breadcrumb = []
        current_folder = folder
        while current_folder is not None:
            breadcrumb.append({'url': reverse("folderView", args=[current_folder.pk]), 'title': current_folder.title})
            current_folder = current_folder.parent
        return breadcrumb[::-1]
    
    breadcrumb = get_breadcrumb(request, folder)

    context = {
        'form': folder_form,
        'fileform': file_form,
        'folders': folderChildren,
        'files': files,
        'favfolders': favfolders,
        'breadcrumb': breadcrumb
    }

    return render(request, 'filemanager/home.html', context)