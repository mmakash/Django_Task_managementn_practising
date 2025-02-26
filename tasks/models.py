from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField(blank=True,null=True)
        start_date = models.DateField()

        def __str__(self):
            return self.name

class Task(models.Model):
    STATUS_CHOICES = [
         ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE,default=1)
    assigned_to = models.ManyToManyField(Employee,related_name="tasks")
    tite = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='PENDING')
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tite

class TaskDetails(models.Model):
    High = 'H'
    Medium = 'M'
    Low = 'L'

    PRIORITY_OPTIONS = (
        (High, 'High'),
        (Medium, 'Medium'),
        (Low, 'Low'),
    )
    task = models.OneToOneField(Task, on_delete=models.CASCADE,related_name="details")
    # assigned_to = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=PRIORITY_OPTIONS,default=Low)
    notes = models.TextField(blank=True,null=True)

    def __str__(self):
        return f"Detais of {self.task.tite}"

#signals
@receiver(post_save, sender=Task)
def notify_task_creation(sender, instance,created, **kwargs):
    if created:
        print("Sender:",sender)
        print("Instance:",instance)
        print(kwargs)
        instance.is_cmpleted = False
        instance.save()
        print("Task is created")


