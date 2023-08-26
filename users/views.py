from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import LoginForm, RegisteationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.views import LoginView,LogoutView,TemplateView
# Create your views here.

class RegisterView(CreateView):
    form_class = RegisteationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)
    

class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('ads_list')
    
class LogoutView(LogoutView):
    next_page = reverse_lazy('ads_list')
    


class ProfileView(TemplateView):
    template_name = 'profile.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context