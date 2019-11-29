from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from students.models import Students



def logout_(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    s = Students.objects.all()
    return render(request,'index.html',{"sts": s})

@login_required(login_url='login')
def csit(request):
    s= Students.objects.filter(faculty = 'csit')
    return render(request , 'csit.html',{"sts":s})


@login_required(login_url='login')
def bca(request):
    s= Students.objects.filter(faculty = 'bca')
    return render(request , 'bca.html', {'sts':s})

def login_(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST['pass1']

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            messages.add_message(request, messages.ERROR, 'Username | Password Incorrect')
            return redirect('login')


