# Generated by Django 4.0 on 2022-03-01 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0015_remove_task_dislikes_remove_task_likes_task_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_done',
            field=models.BooleanField(default=False),
        ),
    ]
