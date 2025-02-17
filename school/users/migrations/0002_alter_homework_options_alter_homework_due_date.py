# Generated by Django 5.1.4 on 2024-12-21 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homework',
            options={'permissions': [('is_teacher', 'Can add homeworks to do')]},
        ),
        migrations.AlterField(
            model_name='homework',
            name='due_date',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=100),
        ),
    ]
