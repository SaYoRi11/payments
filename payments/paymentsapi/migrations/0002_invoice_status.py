# Generated by Django 3.2.7 on 2021-10-07 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentsapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='status',
            field=models.CharField(choices=[('Rejected', 'Rejected'), ('Approved', 'Approved'), ('Pending', 'Pending')], default='Pending', max_length=20),
            preserve_default=False,
        ),
    ]
