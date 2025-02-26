from django.shortcuts import render,redirect
from django.http import HttpResponse
from tasks.forms import TaskForm,TaskModelForm,TaskDetailsModelForm
from tasks.models import Employee, Task
from django.db.models import Count, Q
from datetime import datetime
from django.contrib import messages



# Create your views here.
def manager_dashboard(request):
    type = request.GET.get('type','all')
   
    counts = Task.objects.aggregate(total= Count('id'),
                                    completed=Count('id',filter=Q(status="COMPLETED")),
                                    inprogress=Count('id',filter=Q(status="IN_PROGRESS")),
                                    pending=Count('id',filter=Q(status="PENDING")))
    
    base_query = Task.objects.select_related('details').prefetch_related('assigned_to')

    if type == 'completed':
        tasks = base_query.filter(status="COMPLETED")
    elif type == 'inprogress':
        tasks = base_query.filter(status="IN_PROGRESS")
    elif type == 'pending':
        tasks = base_query.filter(status="PENDING")
    elif type == 'all':
        tasks = base_query.all()
    

    context = {
        "tasks":tasks,
        "counts":counts
    }
    return render(request,'dashboard/manager-dashboard.html',context)

def user_dashboard(request):
    return render(request,'dashboard/user-dashboard.html')

def test(request):
    context = {
        "name": ["asif", "ahmed", "mohamed"],
        "age": [10, 20, 30]
    }
    return render(request,'test.html',context)

def create_task(request):
  
    form = TaskModelForm()
    task_details_form = TaskDetailsModelForm()

    if request.method == "POST":
        form = TaskModelForm(request.POST)
        task_details_form = TaskDetailsModelForm(request.POST)
        if form.is_valid() and task_details_form.is_valid():
            task = form.save()
            task_detail = task_details_form.save(commit=False)
            task_detail.task = task
            task_detail.save()

            # task.save() 
            # form.save_m2m() 
            messages.success(request, "Task created successfully")
            return redirect('create-task')
    context = {
        "form": form,
        "task_details_form": task_details_form
    }
    return render(request, 'task_form.html', context)
def update_task(request,id):
    task = Task.objects.get(id=id)
    form = TaskModelForm(instance=task)

    if task.details:
        task_details_form = TaskDetailsModelForm(instance=task.details)

    if request.method == "POST":
        form = TaskModelForm(request.POST,instance=task)
        task_details_form = TaskDetailsModelForm(request.POST,instance=task.details)
        if form.is_valid() and task_details_form.is_valid():
            task = form.save()
            task_detail = task_details_form.save(commit=False)
            task_detail.task = task
            task_detail.save()
           

            # task.save() 
            # form.save_m2m() 
            messages.success(request, "Task updated successfully")
            return redirect('update-task',id=id)
    context = {
        "form": form,
        "task_details_form": task_details_form
    }
    return render(request, 'task_form.html', context)


def delete_task(request,id):
    if request.method == "POST":
        task = Task.objects.get(id=id)
        task.delete()
        messages.success(request, "Task deleted successfully")
        return redirect('manager-dashboard')

def view_task(request):
    # retrieve all task
    # tasks = Task.objects.all()
    # retrieve specefic task
    # task_3 = Task.objects.get(id=3)
    # retrieve first task
    # first_task = Task.objects.first()
    # 1. Show the tasks assigned to a specific employee
    employee = Employee.objects.get(name="Debra Williams")
    tasks = employee.tasks.all()
    print(tasks)
    # for task in tasks:
    #     print(task.tite,task.status)

    return render(request,'show_task.html',{"tasks":tasks})