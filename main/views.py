from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect, Http404
from . import forms


def index(request):
  return render(request, "index.html", None)


class RegisterForm(FormView):
  form_class = forms.RegisterUserForm
  success_url = '/register/'
  template_name = 'register.html'
  
  def form_valid(self, form):
    form.save()
    
    return super().form_valid(form)
  
class LoginForm(FormView):
  form_class = forms.LoginForm
  success_url = '/login/'
  template_name = 'login.html'
  
  def form_valid(self, form):
    self.user = form.get_user()
    login(self.request, self.user)
    
    return super().form_valid(form)
  