# Generated by Django 5.0.6 on 2024-06-19 03:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_user_id'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user_id',
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
