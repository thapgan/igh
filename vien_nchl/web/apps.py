from django.apps import AppConfig


class WebConfig(AppConfig):
    name = 'vien_nchl.web'
    verbose_name = "Web"

    def ready(self):
        pass
