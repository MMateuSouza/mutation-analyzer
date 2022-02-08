# Generated by Django 4.0.2 on 2022-02-08 00:58

from django.conf import settings
from django.contrib.auth.models import User
from django.db import migrations


def create_superuser_credentials(apps, schema_editor):
    administrator = User(
        first_name='Administrador', last_name='de Sistemas', username=settings.DEFAULT_ADMINISTRATOR_USERNAME,
        email=settings.DEFAULT_ADMINISTRATOR_EMAIL, is_staff=True, is_superuser=True, is_active=True
    )
    administrator.set_password(settings.DEFAULT_ADMINISTRATOR_PASSWORD)
    administrator.save()


class Migration(migrations.Migration):

    dependencies = [
        ('mutation_analyzer', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser_credentials),
    ]