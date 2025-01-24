from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Команда создания суперпользователя"""

    def handle(self, *args, **options):
        email = str(input('Почта: '))
        first_name = str(input('Имя: '))
        last_name = str(input('Фамилия: '))
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
            first_name=first_name,
            last_name=last_name,
            job_title='пользователь',
            is_staff=True,
            is_superuser=False,
            is_active=True
        )

        user.set_password(password)
        user.save()
        print('\nПрофиль пользователя создан.\n')
