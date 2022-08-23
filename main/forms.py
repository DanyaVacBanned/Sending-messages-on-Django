from .models import users, messages
from django.forms import ModelForm, TextInput, DateTimeInput

class UserForm(ModelForm):
    class Meta:
        model = users
        fields = ['user_name', 'mail']

        widgets = {
            'user_name': TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Имя пользователя'
            }),
            'mail': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта пользователя'
            }),
        }


class Messages(ModelForm):
    class Meta:
        model = messages
        fields = ['message_id', 'message_text', 'message_datetime']

        widgets = {
            'message_id': TextInput(attrs= {
                'class': 'message-form',
                'placeholder': 'ID сообщения'
            }),
            'message_text': TextInput(attrs={
                'class': 'message-form',
                'placeholder': 'Текст сообщения'
            }),
            'message_datetime': DateTimeInput(attrs={
                'class': 'message-form',
                'placeholder': 'Дата и время'
            }),
        }
