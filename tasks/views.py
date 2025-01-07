from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1 style='color:red'>wellcome to the task management system</h1>")

def contact(request):
    return HttpResponse("<h1 style='color:red'>contact with us</h1>")

def show_tasks(request):
    return HttpResponse("<h1 style='color:red'>This is show tasks page</h1>")
