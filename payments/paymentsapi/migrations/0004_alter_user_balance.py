# Generated by Django 3.2.7 on 2021-10-07 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentsapi', '0003_alter_invoice_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='balance',
            field=models.FloatField(default=0),
        ),
    ]
