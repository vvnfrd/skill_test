from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Команда создания суперпользователя"""

    def handle(self, *args, **options):

        email = str(input('Почта: '))

        while True:
            password1 = str(input('Пароль: '))
            password2 = str(input('Подтвердите пароль: '))
            if password1 == password2:
                password = password2
                break
            else:
                print('\nПароли не совпадают, попробуйте ещё раз.\n')

        user = User.objects.create(
            email=email,
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        user.set_password(password)
        user.save()
        print('\nПрофиль администратора создан.\n')