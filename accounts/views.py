from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms

class SignUp(CreateView):
    form_class=forms.UserCreationFormqwq
    template_name='accounts/signup.html'
    success_url=reverse_lazy('login')
    


# Create your views here.
