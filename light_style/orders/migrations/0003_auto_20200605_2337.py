# Generated by Django 3.0.5 on 2020-06-05 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200605_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='productinbasket',
            name='price_per_item',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='productinbasket',
            name='total_price',
            field=models.FloatField(default=0),
        ),
    ]
