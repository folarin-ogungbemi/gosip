# Generated by Django 3.2.16 on 2022-12-30 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='country',
            new_name='user_country',
        ),
    ]