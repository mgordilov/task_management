# Generated by Django 5.0.1 on 2024-02-04 18:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('tm_app', '0002_user_department_task_userprofile_delete_auth_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.OneToOneField(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
