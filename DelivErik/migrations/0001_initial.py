# Generated by Django 3.1.7 on 2021-03-25 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_unique_ID', models.IntegerField()),
                ('customer_first_name', models.CharField(max_length=30)),
                ('customer_last_name', models.CharField(max_length=30)),
                ('customer_first_line_address', models.IntegerField()),
                ('customer_second_line_address', models.TextField()),
                ('customer_postcode', models.TextField()),
                ('customer_email_address', models.EmailField(max_length=254)),
                ('customer_phone_number', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parcel_unique_ID', models.IntegerField()),
                ('parcel_width', models.IntegerField()),
                ('parcel_height', models.IntegerField()),
                ('parcel_length', models.IntegerField()),
                ('parcel_weight', models.IntegerField()),
                ('parcel_description', models.TextField()),
                ('parcel_status_update_time', models.DateField()),
                ('parcel_status', models.CharField(choices=[('R', 'Recieved'), ('C', 'Collected'), ('D', 'Delivered'), ('X', 'Cancelled')], max_length=1)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DelivErik.customer')),
            ],
        ),
    ]
