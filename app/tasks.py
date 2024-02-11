from django_cron import CronJobBase, Schedule
from django.core.mail import send_mail
from .models import Todo
from django.utils import timezone
from datetime import timedelta

class SendNotificationEmails(CronJobBase):
    RUN_EVERY_MINS = 1 # Run task every hour

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    # code = 'your_app.send_notification_emails'  # A unique code for your task
    code = 'app.send_notification_emails' 

    def do(self):
        # Retrieve clients with pending todos
        # Send notification mail to user before inform_before time from the end time of the todo if the todo is not completed and if end time is available
        todos = Todo.objects.all()
        for todo in todos:
            if todo.completed == False and todo.end != None:
                # Check for the time to send mail before inform_before time from the end time of the todo
                if todo.inform_before != 0 and todo.end - timezone.now() <= timedelta(minutes=todo.inform_before):
                    # send mail to user
                    send_mail(
                        'Todo Reminder',
                        f'You have a todo {todo.title} at {todo.end} .',
                        'fayispvchelari@gmail.com',
                        [todo.email],
                        fail_silently=False,
                    )
                    
