from django.shortcuts import render,redirect
from . models import *
from . forms import *

# Create your views here.
def todo(request):
    tasks=Task.objects.all()
    form=TaskForm()
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={'tasks':tasks,'form':form}
    return render(request,'list.html',context)

def updateTask(request,pk):
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)
    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={'form':form}
    return render(request,'UpdateTask.html',context)

def deleteTask(request,pk):
    item=Task.objects.get(id=pk)
    context={'item':item}
    if request.method=='POST':
        item.delete()
        return redirect('/')
    return render(request,'deleteTask.html',context)