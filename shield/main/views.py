from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView

from .forms import *
import string, random, hashlib, zlib



def home(request):
    return render(request, 'main/home.html')


class PasswordGeneratorView(FormView, LoginRequiredMixin):
    login_url = '/authentication/'
    template_name = 'main/password_generator.html'
    form_class = PasswordForm

    def form_valid(self, form):
        length = form.cleaned_data['length']
        uppercase = form.cleaned_data['uppercase']
        lowercase = form.cleaned_data['lowercase']
        special_chars = form.cleaned_data['special_chars']
        digits = form.cleaned_data['digits']

        characters = ''
        if uppercase:
            characters += string.ascii_uppercase
        if lowercase:
            characters += string.ascii_lowercase
        if special_chars:
            characters += string.punctuation
        if digits:
            characters += string.digits

        if not characters:
            form.add_error(None, 'Вы должны выбрать хотя бы один параметр для генерации пароля.')
            return self.form_invalid(form)

        password = ''.join(random.choice(characters) for i in range(length))

        return render(self.request, 'main/password_generator.html',
                      {'form': form, 'password': password})


class EncryptionView(FormView, LoginRequiredMixin):
    login_url = '/authentication/'
    template_name = 'main/encryption.html'
    form_class = EncryptionForm

    def form_valid(self, form):
        text = form.cleaned_data['text']
        encryption_type = form.cleaned_data['encryption_type']

        if encryption_type == 'md5':
            result = hashlib.md5(text.encode()).hexdigest()
        elif encryption_type == 'crc32':
            result = hex(zlib.crc32(text.encode()))
        elif encryption_type == 'sha1':
            result = hashlib.sha1(text.encode()).hexdigest()
        elif encryption_type == 'sha256':
            result = hashlib.sha256(text.encode()).hexdigest()
        elif encryption_type == 'sha512':
            result = hashlib.sha512(text.encode()).hexdigest()

        return render(self.request, 'main/encryption.html', {'form': form, 'result': result})

class UserRegistration(CreateView):
    form_class = UserRegistrationForm
    template_name = 'main/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UserLogin(LoginView):
    form_class = UserLoginForm
    template_name = 'main/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
