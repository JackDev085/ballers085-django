from django.apps import AppConfig


class HelloConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ballers085"


# from django.apps import AppConfig
# class YourAppNameConfig(AppConfig):
#     name = 'your_app_name'
#     def ready(self):
#         import your_app_name.signals
