# Generated by Django 3.1.7 on 2021-03-25 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DelivErik', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_unique_ID',
            field=models.CharField(max_length=30),
        ),
    ]
