# Generated by Django 3.1.4 on 2023-04-21 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20230421_1337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='address',
        ),
        migrations.AddField(
            model_name='lead',
            name='country',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]