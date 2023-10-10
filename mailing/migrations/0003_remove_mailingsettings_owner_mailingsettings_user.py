# Generated by Django 4.2.5 on 2023-10-07 21:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailing', '0002_mailingsettings_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailingsettings',
            name='owner',
        ),
        migrations.AddField(
            model_name='mailingsettings',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]