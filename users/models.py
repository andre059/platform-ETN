from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """Пользователь"""

    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    phone_number = models.CharField(max_length=15, verbose_name='номер телефона', **NULLABLE)
    country = models.CharField(max_length=50, **NULLABLE, verbose_name='страна')
    city = models.CharField(max_length=100, **NULLABLE, verbose_name='город')
    date_of_birth = models.DateField(**NULLABLE, verbose_name='дата рождения')
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='аватар')

    is_active = models.BooleanField(default=True, verbose_name='активный')
    is_authorized = models.BooleanField(default=False, verbose_name='Пользователь авторизован')
    is_authenticated = models.BooleanField(default=False, verbose_name='Пользователь аутентифицирован')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.phone_number}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
