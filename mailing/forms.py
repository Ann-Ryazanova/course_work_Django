from django import forms

from client.models import Client
from mailing.models import MailingSettings


class MailingSettingsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(MailingSettingsForm, self).__init__(*args, **kwargs)

        # Ограничиваем queryset для выбора клиентов только теми, которых создал текущий пользователь
        self.fields['clients'].queryset = Client.objects.filter(user=user)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    class Meta:
        model = MailingSettings
        fields = ('topic_mail', 'body_mail', 'clients',
                  'period', 'time', 'day', 'status',)
