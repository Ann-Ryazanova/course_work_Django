from django import forms
from django.conf import settings
from django.forms import DateField, DateTimeField

from mailing.models import MailingSettings


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingSettingsForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = MailingSettings
        fields = ('topic_mail', 'body_mail', 'clients',
                  'period', 'time', 'day', 'status',)
