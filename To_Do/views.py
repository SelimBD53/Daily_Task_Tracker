from django.shortcuts import render, redirect
from To_Do.forms import TaskModelForm
from To_Do.models import TaskModel
# Create your views here.




def store_tasks(request):
    if request.method == "POST":
        task = TaskModelForm(request.POST)
        if task.is_valid():
            task.save()
            # print(task.cleaned_data)
            return redirect('show_task')
    else:
        task = TaskModelForm()
    return render(request, 'store_task.html', {'form': task})


def show_task(request):
    tasks = TaskModel.objects.all()
    return render(request, 'show_task.html', {'data': tasks})


def is_completed(request, id):
    task = TaskModel.objects.get(pk=id)
    task.is_completed = True
    task.save()
    return redirect('show_task')
   


def task_completed(request):
    task = TaskModel.objects.all()
    return render(request, 'completed.html', {"task": task})



def delete_task(request, id):
    task = TaskModel.objects.get(pk=id).delete()
    return redirect('show_task')
    
    
def edit_task(request, id):
    task = TaskModel.objects.get(pk=id)
    form = TaskModelForm(instance=task)
    if request.method == 'POST':
        pass
        