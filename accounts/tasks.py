from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string


@shared_task
def send_registration_email(recipient_email: str, template_name: str, data: dict, subject: str) -> None:
    """
    Отправляет письмо для подтверждения определенных действий.
    """

    message = render_to_string(template_name=template_name, context=data)
    send_mail(
        subject=subject,
        message=message,
        from_email='admin@ourweb.com',
        recipient_list=[recipient_email],
        fail_silently=True
    )
