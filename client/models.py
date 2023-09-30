from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    # Тот, кто получает письмо должен быть
    email = models.EmailField(unique=True, verbose_name='почта')

    first_name = models.CharField(max_length=100, verbose_name='Имя', **NULLABLE)
    last_name = models.CharField(max_length=100, verbose_name='Фамилия', **NULLABLE)
    middle_name = models.CharField(max_length=100, verbose_name='Отчество', **NULLABLE)
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    #Должно ли быть поле владелец клиента


    def __str__(self):
        return self.email
                #f'{self.first_name}, {self.last_name}'
                #f'{self.middle_name}, {self.comment}')

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
