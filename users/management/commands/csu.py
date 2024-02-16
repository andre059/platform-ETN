from decouple import config
from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@mail.ru',
            first_name='Admin',
            last_name='Adminich',
            is_active=True,
            is_staff=True,
            is_superuser=True,
            is_authorized=True,
            is_authenticated=True
        )

        password = config('CSU_SET_PASSWORD')
        user.set_password(password)
        user.save()
