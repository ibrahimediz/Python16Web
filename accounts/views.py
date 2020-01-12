from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class Signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('hosgeldin')
    template_name = 'signup.html'
