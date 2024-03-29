from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class RangeInput(forms.TextInput):
    input_type = 'range'

class PasswordForm(forms.Form):
    length = forms.IntegerField(
        label='Длина пароля',
        widget=RangeInput(attrs={'min': 8, 'max': 40, 'class': 'length-class', 'oninput': 'updateLength(this.value)'})
    )
    uppercase = forms.BooleanField(
        label='Буквы в верхнем регистре',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'uppercase-class'})
    )
    lowercase = forms.BooleanField(
        label='Буквы в нижнем регистре',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'lowercase-class'})
    )
    special_chars = forms.BooleanField(
        label='Специальные символы',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'special-chars-class'})
    )
    digits = forms.BooleanField(
        label='Цифры',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'digits-class'})
    )

    def clean(self):
        cleaned_data = super().clean()
        if not any(cleaned_data.values()):
            raise forms.ValidationError("Вы должны выбрать хотя бы один параметр для генерации пароля.")


class EncryptionForm(forms.Form):
    text = forms.CharField(label='Текст для шифрования', widget=forms.Textarea)
    encryption_type = forms.ChoiceField(
        label='Тип шифрования',
        choices=[
            ('md5', 'MD5'),
            ('crc32', 'CRC32'),
            ('sha1', 'SHA1'),
            ('sha256', 'SHA256'),
            ('sha512', 'SHA512'),
        ]
    )

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'username-input'}))
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={'class': 'user-email'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'password-1'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'password-2'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'username-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'password'}))



