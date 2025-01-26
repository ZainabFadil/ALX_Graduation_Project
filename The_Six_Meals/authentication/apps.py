from django.apps import AppConfig
from django.apps import AppConfig


class AuthConfig(AppConfig):
    # Specifies the default primary key field type for models in this app
    default_auto_field = 'django.db.models.BigAutoField'
    # Defines the name of the Django app that will be used in the Django admin interface
    name = 'authentication'
