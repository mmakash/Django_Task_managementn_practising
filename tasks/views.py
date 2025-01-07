from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1 style='color:red'>wellcome to the task management system</h1>")

def contact(request):
    return HttpResponse("<h1 style='color:red'>contact with us</h1>")

def show_tasks(request):
    return HttpResponse("<h1 style='color:red'>This is show tasks page</h1>")

def show_specefic_task(request,id):
    print('id',id)
    print('type: ',type(id))
    return HttpResponse(f"<h1 style='color:red'>This is show specefic task page: {id}</h1>")


def about(request):
    return HttpResponse("<h1 style='color:red'>This is about page</h1>")
