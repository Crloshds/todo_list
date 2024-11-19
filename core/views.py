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

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'update-task.html', context)



    