# Generated by Django 5.1.5 on 2025-01-31 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.BooleanField(db_default=False, default=False),
        ),
    ]
