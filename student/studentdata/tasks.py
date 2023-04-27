from time import sleep
from student.settings import EMAIL_HOST_USER
from celery import shared_task
from django.core.mail import send_mail


@shared_task()
def send_feedback_email_task(email_address, message):
    """Sends an email when the feedback form has been submitted."""
    sleep(20)  # Simulate expensive operation that freezes Django
    send_mail(
        "Your Feedback",
        f"\t{message}\n\nThank you!",
        EMAIL_HOST_USER,
        [email_address],
        fail_silently=False,
    )