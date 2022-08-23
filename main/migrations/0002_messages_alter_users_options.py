# Generated by Django 4.1 on 2022-08-23 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='messages',
            fields=[
                ('message_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id сообщения')),
                ('message_text', models.TextField(verbose_name='Текст сообщения')),
                ('message_datetime', models.DateTimeField(verbose_name='Дата и время сообщения')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
