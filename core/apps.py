# core/apps.py
from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name = 'Fintech Core'

    def ready(self):
        try:
            import core.signals  # If you add signals later
        except ImportError:
            pass
