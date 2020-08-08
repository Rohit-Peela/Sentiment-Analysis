
from django.contrib import messages

from django.shortcuts import redirect
from .models import Reg
from .forms import LoginForm
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
import base64
from django.core.files.base import ContentFile
from subprocess import Popen, PIPE
import json
import os
from textblob import TextBlob


def registration(request):

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
           form.save()
           print("valid Details")
           messages.success(request, "Account created successfully!")
           return redirect('login')

    else:
            form = RegistrationForm()
            print("Invalid Details")

    return render(request, 'registration.html', {'form':form})


def login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            un = request.POST.get('username')
            pwd = request.POST.get('password')
            dbuser=Reg.objects.filter(username=un,password=pwd)
            if not dbuser:
                return HttpResponse("Login Failed")
            else:
                return redirect('index')
        else:
            form = LoginForm(request.POST)
            return render(request, 'login.html', {'form':form})
    else:
        form = LoginForm(request.POST)
        return render(request, 'login.html', {'form':form})


def index(request):
    return render(request, 'parent.html')

def feature(request):
    return render(request, 'feature.html')

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def process_word(request):
    para = request.POST.get('review')
    para = (TextBlob(str(para))).polarity
    if float(para) > 0:
	    return HttpResponse(True)
    else:
    	return HttpResponse(False)

def features(request):
    return render(request, 'feature.html')
