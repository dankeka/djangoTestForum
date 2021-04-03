from django.shortcuts import render
from . import forms

async def index(request):
  return render(request, "index.html", None)

async def register(request):
  if request.method == "GET":
    form = forms.RegisterUserForm()
    return render(request, "register.html", {"form": form})
  else:
    pass