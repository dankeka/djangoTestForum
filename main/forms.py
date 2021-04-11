from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from . import models as mod

class RegisterUserForm(UserCreationForm):
  email = forms.EmailField(max_length=50)
  
  def __init__(self, *args, **kwargs):
    super(RegisterUserForm, self).__init__(*args, **kwargs)

    for fieldname in ('username', 'email', 'password1', 'password2'):
      self.fields[fieldname].help_text = None
      self.fields[fieldname].widget.attrs.update({'class': 'form-control'})
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
  def __init__(self, *args, **kwargs):
    super(LoginForm, self).__init__(*args, **kwargs)

    for fieldname in ('username', 'password'):
      self.fields[fieldname].widget.attrs.update({'class': 'form-control'})
  class Meta:
    model = User
    fields = ('username', 'password')
    

class AddMsgForm(forms.ModelForm):
  class Meta:
    model = mod.Message
    fields = ('text',)
    
  def __init__(self, *args, **kwargs):
    super(AddMsgForm, self).__init__(*args, **kwargs)
    
    for fieldname in ('text',):
      self.fields[fieldname].widget.attrs.update({'class': 'form-control'})
      

class AddThemeForm(forms.Form):
  title = forms.CharField(label='Название', max_length=60, required=True)
  sectionPk = forms.CharField(widget=forms.HiddenInput())
    
  def __init__(self, value=None, *args, **kwargs):
    super(AddThemeForm, self).__init__(*args, **kwargs)
    
    if value:
      self.fields['sectionPk'].initial = value
    
    for fieldname in ('title',):
      self.fields[fieldname].widget.attrs.update({'class': 'form-control'})
