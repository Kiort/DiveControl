from django.apps import AppConfig


class DiveappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'diveapp'

class DiveAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'diveapp'

    def ready(self):
        import diveapp.signals 