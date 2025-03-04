from django.db.models.signals import m2m_changed,post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Task

#signals
@receiver(m2m_changed, sender=Task.assigned_to.through)
def notify_employee_on_task_creation(sender, instance,action, **kwargs):
    if action == "post_add":
        assigned_email = [emp.email for emp in instance.assigned_to.all()]
        print(assigned_email)
        
        send_mail(
            'New Task Assigned',
            f"You have been assigned a task {instance.tite}",
            'musaddekurakash@gmail.com',
            assigned_email,
            fail_silently=False,    
        )


@receiver(post_delete, sender=Task)
def delete_associated_details(sender, instance, **kwargs):
    if instance.details:
        print(instance)
        instance.details.delete()
        print("Details deleted")