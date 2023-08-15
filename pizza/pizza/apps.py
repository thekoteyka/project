from django.apps import AppConfig


class PizzaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pizza'
    verbose_name = "Pizza recipes"
