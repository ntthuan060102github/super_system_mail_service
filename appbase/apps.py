from django.apps import AppConfig
from pkg_helpers.services.service_route import MAIL_ROUTE

class AppbaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appbase'
    api_prefix = f"{MAIL_ROUTE}/"
