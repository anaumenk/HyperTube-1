# Generated by Django 2.0.7 on 2018-10-17 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_player', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='torrentmodel',
            name='film',
        ),
    ]
