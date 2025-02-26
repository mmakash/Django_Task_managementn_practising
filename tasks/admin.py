from django.contrib import admin
from .models import Task,TaskDetails,Employee,Project
admin.site.register(Task)
admin.site.register(TaskDetails)
admin.site.register(Employee)
admin.site.register(Project)

# Register your models here.
