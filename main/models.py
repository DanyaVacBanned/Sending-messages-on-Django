from django.db import models

class users(models.Model):
    user_name = models.CharField('Имя пользователя', max_length=40)
    mail = models.CharField('Почта пользователя', max_length=100)



    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = "Пользователи"


class messages(models.Model):
    message_id = models.IntegerField('Id сообщения', primary_key=True)
    message_text = models.TextField('Текст сообщения')
    message_datetime = models.DateTimeField('Дата и время сообщения')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

