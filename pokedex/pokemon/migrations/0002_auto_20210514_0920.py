# Generated by Django 3.2.3 on 2021-05-14 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='order',
        ),
        migrations.RemoveField(
            model_name='type',
            name='order',
        ),
    ]
