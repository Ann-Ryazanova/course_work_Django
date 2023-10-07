from datetime import timedelta

from mailing.models import MailingSettings


def install_next_date(mail: MailingSettings):
    if mail.period == mail.PERIOD_DAILY:
        mail.day += timedelta(1)
    elif mail.period == mail.PERIOD_WEEKLY:
        mail.day += timedelta(7)
    else:
        mail.day += timedelta(30)

    return mail.day
