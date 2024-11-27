from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Task
from . forms import TaskForm


def index(request):
    task_list = Task.objects.all()
    form = TaskForm

    context = {
        'task_list': task_list,
        'form': form
        }

    return render(request, "index.html", context)

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            task_list = Task.objects.all()
            form = TaskForm()

            context = {
                'task_list': task_list,
                'form': form
                }
            return HttpResponse(render(request, 'create_task.html', context))

    return render(request, 'create_task.html', {'form': form})

def close_modal(request):
    return HttpResponse('')

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        task.delete()
        task_list = Task.objects.all()
        return HttpResponse(render(request, 'task_table.html', {'task_list': task_list}))

    context = {
        'task': task
        }
    
    return render(request, 'confirm_delete.html', context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)
    task_list = Task.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'task_list': task_list, 'form': form }

    return render(request, 'update_task.html', context)




    