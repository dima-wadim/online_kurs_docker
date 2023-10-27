from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='kantora.mwn@gmail.com',
            first_name='Вадим',
            last_name='Машков',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        user.set_password('Vdy1970*')
        user.save()