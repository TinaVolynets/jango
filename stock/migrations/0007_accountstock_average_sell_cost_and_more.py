# Generated by Django 5.0 on 2024-01-23 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_account_accountcurrency_accountstock'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountstock',
            name='average_sell_cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='accountstock',
            name='average_buy_cost',
            field=models.IntegerField(default=0),
        ),
    ]
