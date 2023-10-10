from django.contrib import admin

from mailing.models import MailingSettings, Logs


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    list_display = ('status',
                    'topic_mail', 'body_mail',)
    list_filter = ('status',)


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'status_send', 'last_attempt_send',)
