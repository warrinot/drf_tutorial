# Generated by Django 3.1.2 on 2021-04-08 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='ownder',
            new_name='owner',
        ),
    ]
