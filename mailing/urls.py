from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import MailingSettingsListView, MailingSettingsCreateView, MailingSettingsDetailView, \
    MailingSettingsUpdateView, MailingSettingsDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path('create/', MailingSettingsCreateView.as_view(), name='create_mailing'),
    path('', MailingSettingsListView.as_view(), name='list'),
    #path('contact/', MailingContactView.as_view(), name='contacts'),
    path('product/<int:pk>/', MailingSettingsDetailView.as_view(), name='mailing_detail'),
    path('edit/<int:pk>/', MailingSettingsUpdateView.as_view(), name='update_mailing'),
    path('delete/<int:pk>/', MailingSettingsDeleteView.as_view(), name='delete_mailing'),
]
