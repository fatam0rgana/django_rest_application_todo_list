from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/login'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home.homepage')
        return super().get(request, *args, **kwargs)


class LogoutInterfaceView(LogoutView):
    template_name = 'home/login.html'


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home/welcome.html'
    login_url = '/login'

