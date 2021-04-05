from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView, View
from django.http import HttpResponseRedirect, Http404
from . import forms
from . import models as md


def index(request):
  sections = md.Section.objects.all()
  
  context = {
    'sections': sections
  }
  return render(request, "index.html", context)


class RegisterForm(FormView):
  form_class = forms.RegisterUserForm
  success_url = 'login/'
  template_name = 'register.html'
  
  def form_valid(self, form):
    form.save()
    
    return super().form_valid(form)


class LoginForm(FormView):
  form_class = forms.LoginForm
  success_url = '/'
  template_name = 'login.html'
  
  def form_valid(self, form):
    self.user = form.get_user()
    login(self.request, self.user)
    
    return super().form_valid(form)
  

def logout(request):
  django_logout(request)

  return HttpResponseRedirect('/')


def section(request, pk):
  section = md.Section.objects.get(pk = pk)
  
  themes = md.Theme.objects.filter(section = section)
  
  context = {
    'section': section,
    'themes': themes
  }
  return render(request, "section.html", context)


def theme(request, pk):
  pass