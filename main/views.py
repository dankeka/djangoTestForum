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
  
  form = forms.AddThemeForm(pk)
  
  context = {
    'section': section,
    'themes': themes,
    'form': form
  }
  return render(request, "section.html", context)


def theme(request, pk):
  theme = md.Theme.objects.get(pk = pk)
  
  messages = md.Message.objects.filter(theme = theme)
  
  form = forms.AddMsgForm()
  
  context = {
    'theme': theme,
    'messages': messages,
    'form': form
  }
  return render(request, "theme.html", context)


def addMsg(request):
  if request.user.is_authenticated:
    themePk = request.POST["themePk"]
    text = request.POST["text"]
    user = request.user
    
    try:
      theme = md.Theme.objects.get(pk = themePk)
      
      newMsg = md.Message.objects.create(theme=theme, user=user, text=text)
      newMsg.save()
    except:
      raise Http404
    
    return HttpResponseRedirect(f'/theme/{themePk}/')
  else:
    raise Http404
  

def addTheme(request):
  if request.user.is_authenticated:
    try:
      reqData = {
        'sectionPk': request.POST['sectionPk'],
        'title': request.POST['title'],
        'user': request.user
      }
      
      section = md.Section.objects.filter(pk=reqData["sectionPk"]).first()
      
      newTheme = md.Theme.objects.create(
        title=reqData["title"],
        section=section,
        user=reqData["user"]
      )
      newTheme.save()
      
      return HttpResponseRedirect(f"/theme/{newTheme.pk}")
    except:
      raise Http404
  else:
    raise Http404