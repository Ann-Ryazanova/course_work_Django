from django.conf import settings
from django.core.mail import send_mail
from django.core.management import BaseCommand

from mailing.models import MailingSettings


class Command(BaseCommand):
    def handle(self, *args, **options):
        #client_email = MailingSettings.objects.filter(status='AC').values()
        for mail in MailingSettings.objects.filter(status='CR'):
            emails = mail.clients.all()
            print(emails)