from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.management import call_command


def mailing_scheduler():
    return call_command('start_mail')


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(mailing_scheduler, 'interval', seconds=1)
    scheduler.start()
