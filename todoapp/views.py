from django.shortcuts import render,redirect
from . models import todo
from . forms import todoform
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def index(request):
    
    if request.method=="POST":
        form=todoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        task=todo.objects.all()
        form=todoform()
        context={'form':form,'tasks':task,'completed':todo.completed}
    
    return render(request, 'index.html', context)

def delete(request,pk):
    
    data=todo.objects.get(id=pk)
    data.delete()
    return redirect('index')

def update(request,pk):
    instance=todo.objects.get(id=pk)
    form=todoform(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('index')

    context={'form':form,'completed':completed}
    return render(request,'update.html',context)
    
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.success(request, "Invalid credentials !")
            return redirect('login')
    return render(request, 'login.html')

def login2(request):
    context={'form':AuthenticationForm}
    return render(request, 'login2.html', context)

def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        user=User.objects.create_user(username=username,password=password,email=email)
        user.save()
        return redirect('login')
    return render(request,'signup.html')

def signup2(request):
    context={'form':UserCreationForm}
    return render(request, 'signup2.html',context)
    
def logout(request):
    auth.logout(request)
    return redirect('index')


def search(request):
    q=request.GET.get('q')
    task_list=todo.objects.all().filter(Q(task__icontains=q) | Q(description__icontains=q))
    context={'task_list':task_list}
    return render(request,'search.html',context)

def completed(request,task_id):
    task=todo.objects.get(id=task_id)
    task_completed=request.POST.get('completed')
    
    return redirect('index')