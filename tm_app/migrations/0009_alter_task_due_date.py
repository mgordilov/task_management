# Generated by Django 5.0.1 on 2024-02-07 00:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tm_app', '0008_remove_task_assigned_to_alter_task_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2024, 2, 8, 0, 58, 47, 76027, tzinfo=datetime.timezone.utc)),
        ),
    ]
