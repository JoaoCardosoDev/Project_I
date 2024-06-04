from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login

class Signup(FormView):
        template_name="auth/sign.html"
        form_class=UserCreationForm
        success_url=reverse_lazy('login')
        redirect_authenticated_user = True

        def form_valid(self, form):
            user=form.save()
            if user is not None:
                login(self.request, user)
            return super(Signup, self).form_valid(form)

        def get(self, request, *args, **kwargs):
            if self.request.user.is_authenticated:
                return redirect('/')
            return super(Signup, self).form_validget(self, *args, **kwargs)

class Login(LoginView):
    template_name="auth/login.html"
    fields= "__all__"
    redirect_authenticates_user = True
    sucess_url = ""
