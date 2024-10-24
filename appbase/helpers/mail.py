from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template

from pkg_helpers.logging import logger

from appbase.dtos.send_mail_with_template import SendMailWithTemplateDTO

@shared_task
def background_send_mail_with_template(data: dict) -> int:
    try:
        return send_mail_with_template(SendMailWithTemplateDTO(**data))
    except Exception as e:
        logger.exception("background_send_mail_with_template exc=%s", e)
        raise e
    
def send_mail_with_template(data: SendMailWithTemplateDTO) -> int:
    try:
        getattr
        template = get_template(data.template)
        content = template.render(context=data.context)

        return send_mail(
            subject=data.subject,
            message="",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=data.to,
            html_message=content
        )
    except Exception as e:
        logger.exception("send_mail_with_template exc=%s", e)
        raise e