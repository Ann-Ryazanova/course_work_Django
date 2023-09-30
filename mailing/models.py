from django.utils import timezone

from django.db import models

from client.models import Client, NULLABLE
from django.db.models import TextChoices


class Status(TextChoices):
    ACTIVE = 'AC', 'Active'
    FINISHED = 'FI', 'Finished'
    CREATED = 'CR', 'Created'


class Period(TextChoices):
    PERIOD_DAILY = 'DA', 'daily'
    PERIOD_WEEKLY = 'WE', 'weekly'
    PERIOD_MONTHLY = 'MO', 'monthly'


class MailingSettings(models.Model):

    period = models.CharField(max_length=20, choices=Period.choices, verbose_name='периодичность рассылки',
                              default=Period.PERIOD_DAILY)
    status = models.CharField(max_length=20, choices=Status.choices, verbose_name='статус рассылки', default=Status.CREATED)
    time = models.TimeField(verbose_name="Время отправки")

    topic_mail = models.CharField(max_length=100, verbose_name='Тема письма')
    body_mail = models.CharField(max_length=100, verbose_name='Тело письма')

    clients = models.ManyToManyField(Client, verbose_name="Получатель/Получатели")

    # свзь по юзеру
    # models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
    # verbose_name='отправитель')
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='отправитель')

    def __str__(self):
        return (f'{self.period} {self.status} {self.time},'
                f'{self.topic_mail} {self.body_mail}'
                f'{self.clients}')

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'


class Logs(models.Model):
    last_attempt_send = models.DateTimeField(default=None, verbose_name="дата и время последней попытки")
    status_send = models.BooleanField(default=False, verbose_name='Статус попытки')

    # Не понимаю как задать пользователя, которому отправлялось письмо
    mailing = models.ForeignKey('MailingSettings', on_delete=models.CASCADE,
                                verbose_name='Рассылка,которая отправлялась')
    #client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name='Получатель рассылки')

    last_attempt_response = models.CharField(max_length=150, **NULLABLE, verbose_name='ответ почтового сервера')

    def __str__(self):
        return (f'{self.last_attempt_send} {self.status_send}'
                f'{self.mailing}')

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
