from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create default user'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='defaultuser').exists():
            User.objects.create_superuser('pythonic', 'email@example.com', 'Ajj!Majji')
            self.stdout.write(self.style.SUCCESS('Successfully created default user'))
