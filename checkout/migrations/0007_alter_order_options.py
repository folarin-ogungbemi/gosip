# Generated by Django 3.2.16 on 2022-12-24 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_alter_orderset_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-order_date']},
        ),
    ]
