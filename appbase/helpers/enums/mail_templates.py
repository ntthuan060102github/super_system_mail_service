from django.db import models

class MailTemplates(models.TextChoices):
    verify_new_user = "verify_new_user.html"