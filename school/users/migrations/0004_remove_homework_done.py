# Generated by Django 5.1.4 on 2024-12-21 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_homework_done'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='done',
        ),
    ]
