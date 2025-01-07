from django.urls import path
from tasks.views import show_tasks,show_specefic_task
urlpatterns = [
    path('show_tasks/',show_tasks),
    path('show_specefic_task/<int:id>/',show_specefic_task)
]