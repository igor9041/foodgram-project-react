from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name']
    USER = 'user'
    ANONYMOUS = 'anonymous'
    ADMIN = 'admin'
    ROLES = [
        (USER, 'Пользователь'),
        (ADMIN, 'Администратор'),
        (ANONYMOUS, 'Аноним'),
    ]

    email = models.EmailField(
        verbose_name='Адрес электронной почты', max_length=150, unique=True,
    )
    username = models.CharField(
        verbose_name='Логин', max_length=150, unique=True,
    )
    first_name = models.CharField(verbose_name='Имя', max_length=150)
    last_name = models.CharField(verbose_name='Фамилия', max_length=150)
    role = models.CharField(
        max_length=30,
        choices=ROLES,
        default=USER,
        verbose_name='Роль'
    )

    @property
    def is_admin(self):
        return self.is_superuser or self.role == CustomUser.ADMIN

    @property
    def is_user(self):
        return self.role == CustomUser.USER

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Follow(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Пользователь',
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Владелец аккаунта',
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = (
            models.constraints.UniqueConstraint(
                fields=('user', 'author', ),
                name='follow_unique'
            ),
        )

    def __str__(self):
        return f'{self.user} => {self.author}'
