from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from studybud import settings

@shared_task(bind=True, time_limit=5)
def send_mail_func(self, subject, message, email):
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )

    return "Sent Mail"