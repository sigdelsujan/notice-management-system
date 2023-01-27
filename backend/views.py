from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from . models import Notice
from django.db import connection
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

cursor = connection.cursor()


# Create your views here.
def index(request):
    allnotices = Notice.objects.raw('SELECT * FROM backend_notice')
    return render(request, 'index.html', {'notices':allnotices})

def user_login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/addnotices")
        else:
            return render(request,'login.html')

    return render(request,'login.html')

@login_required
def add_notice(request):

    if request.method == "POST":
        title = request.POST.get('title')
        desc = request.POST.get('desc')      
        cursor.execute('INSERT INTO backend_notice(title, desc) VALUES(%s, %s)', [title, desc])
        # Notice.objects.raw('INSERT INTO backend_notice(title, desc) VALUES(%s, %s)', [title, desc])
    return render(request,'add_notice.html')
