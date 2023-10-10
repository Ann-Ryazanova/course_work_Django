from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(verbose_name='почта')

    first_name = models.CharField(max_length=100, verbose_name='Имя', **NULLABLE)
    last_name = models.CharField(max_length=100, verbose_name='Фамилия', **NULLABLE)
    middle_name = models.CharField(max_length=100, verbose_name='Отчество', **NULLABLE)
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
