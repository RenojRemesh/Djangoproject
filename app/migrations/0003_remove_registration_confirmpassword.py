# Generated by Django 3.1.7 on 2021-04-28 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210426_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='ConfirmPassword',
        ),
    ]