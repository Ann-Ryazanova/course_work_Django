from datetime import datetime

from django.db import models

from users.models import User
from client.models import Client

NULLABLE = {'blank': True, 'null': True}


class MailingSettings(models.Model):
    PERIOD_DAILY = 'daily'
    PERIOD_WEEKLY = 'weekly'
    PERIOD_MONTHLY = 'monthly'

    PERIODS = (
        (PERIOD_DAILY, 'Ежедневная'),
        (PERIOD_WEEKLY, 'Раз в неделю'),
        (PERIOD_MONTHLY, 'Раз в месяц'),
    )

    STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'
    STATUS_DONE = 'done'

    STATUSES = (
        (STATUS_STARTED, 'Запущена'),
        (STATUS_CREATED, 'Создана'),
        (STATUS_DONE, 'Завершена'),
    )

    period = models.CharField(max_length=20, choices=PERIODS, verbose_name='периодичность рассылки',
                              default=PERIOD_DAILY)
    status = models.CharField(max_length=20, choices=STATUSES, verbose_name='статус рассылки', default=STATUS_CREATED)
    time = models.TimeField(default=datetime.now, verbose_name='время рассылки')
    day = models.DateField(default=datetime.today, verbose_name='Дата начала')
    topic_mail = models.CharField(max_length=100, verbose_name='Тема письма')
    body_mail = models.CharField(max_length=100, verbose_name='Тело письма')

    clients = models.ManyToManyField(Client, verbose_name="Получатель/Получатели")

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)

    def __str__(self):
        return (f'{self.period} {self.status} {self.time},'
                f'{self.topic_mail} {self.body_mail}'
                f'{self.clients}')

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'

        permissions = [
            ('set_status', 'Can change mailing status')
        ]


class Logs(models.Model):
    last_attempt_send = models.DateTimeField(default=None, verbose_name="дата и время последней попытки")
    status_send = models.CharField(max_length=150, verbose_name='Статус попытки')
    mailing = models.ForeignKey('MailingSettings', on_delete=models.CASCADE,
                                verbose_name='Рассылка,которая отправлялась')
    last_attempt_response = models.CharField(max_length=150, **NULLABLE, verbose_name='ответ почтового сервера')

    def __str__(self):
        return (f'{self.last_attempt_send} {self.status_send}'
                f'{self.mailing}')

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
