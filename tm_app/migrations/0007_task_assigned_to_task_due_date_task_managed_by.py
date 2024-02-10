# Generated by Django 5.0.1 on 2024-02-05 00:30

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tm_app', '0006_alter_userprofile_is_manager'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='assigned_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_tasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2024, 2, 6, 0, 30, 17, 650600, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='task',
            name='managed_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
