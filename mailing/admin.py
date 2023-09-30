from django.contrib import admin

from mailing.models import MailingSettings, Logs


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    list_display = ('status',
                    'topic_mail', 'body_mail',)
    list_filter = ('status',)


admin.site.register(Logs)