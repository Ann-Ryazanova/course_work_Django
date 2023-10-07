from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from client.forms import ClientForm
from client.models import Client


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('client:list')