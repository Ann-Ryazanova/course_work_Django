from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from client.models import Client
from mailing.forms import MailingSettingsForm
from mailing.models import MailingSettings
from mailing.services import get_cached_blog


class MailingSettingsListView(ListView):
    model = MailingSettings

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        count_active_mailing = MailingSettings.objects.filter(status=MailingSettings.STATUS_STARTED).count()
        clients_count = Client.objects.values('email').distinct().count()
        context['blog_list'] = get_cached_blog()
        context['count_active_mailing'] = count_active_mailing
        context['clients_count'] = clients_count
        return context


class MailingSettingsDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = MailingSettings

    def test_func(self):
        return self.request.user

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            self.object.user = self.request.user
            self.object.save()

        return super().form_valid(form)


class MailingSettingsCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailing:list')

    def test_func(self):
        return self.request.user

    def get_form_kwargs(self):
        kwargs = super(MailingSettingsCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # Передаем текущего пользователя в форму
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MailingSettingsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailing:list')

    def test_func(self):
        return self.request.user.is_staff or self.get_object().user == self.request.user


class MailingSettingsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('mailing:list')

    def test_func(self):
        return self.request.user.is_superuser or self.get_object().user == self.request.user
