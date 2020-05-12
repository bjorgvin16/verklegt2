from django.apps import AppConfig


class UserprofileConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals