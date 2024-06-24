from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate, logout

from EticDrive.forms import LoginForm

class SignupView(FormView):
    template_name = "auth/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignupView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')
        return super(SignupView, self).get(request, *args, **kwargs)

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print("form is valid")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'filemanager/base.html', {'form': form})

def LogOut(request):
    logout(request)
    return redirect('root')