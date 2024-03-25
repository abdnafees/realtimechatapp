
# Create your views here.
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignUpForm


class LoginView(LoginView):
    template_name = 'account/login.html'


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('login')