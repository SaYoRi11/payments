# Generated by Django 3.2.7 on 2021-10-02 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paymentsapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='cardhholder_name',
            new_name='cardholder_name',
        ),
    ]
