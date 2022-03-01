from datetime import datetime

from celery.schedules import crontab
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from arike.visits.models import VisitDetails

# from config import celery_app
from config.celery_app import app

User = get_user_model()


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour="*", minute=0),
        mail_helper.s(),
    )


@app.task(bind=True)
def mail_helper(self):
    dt = datetime.now()
    for user in User.objects.exclude(email_last_sent=dt.date()).filter(
        email_preff_time__lte=dt.time()
    ):
        send_mail_reminder(user)
        user.email_last_sent = dt.date()
        user.save()


def send_mail_reminder(user):
    print(f"starting to process mail for user {user}")

    visited_count = VisitDetails.objects.filter(
        schedule__nurse=user, schedule__date=datetime.now().date()
    ).count()
    email_content = f"Visited {visited_count} patients today"

    send_mail(
        "Task Status Report",
        email_content,
        "admin@arike.org",
        [user.email],
        fail_silently=False,
    )
    print(f"Completed processing for user {user}")
