from django import forms

from client.models import Client
from mailing.forms import StyleFormMixin


class ClientForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Client
        fields = ('last_name', 'first_name', 'middle_name',
                  'email', 'comment',)