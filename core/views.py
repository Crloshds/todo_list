from django.shortcuts import render, redirect

from .models import Task
from . forms import TaskForm


def index(request):
    form = TaskForm()
    task_list = Task.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'task_list': task_list, 'form': form}

    return render(request, "index.html", context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    task_list = Task.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'task_list': task_list, 'form': form }

    return render(request, 'update-task.html', context)

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task_list = Task.objects.all()

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'task_list': task_list,'task': task}

    return render(request, 'delete-task.html', context)


    