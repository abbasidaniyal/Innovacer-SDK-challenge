# Generated by Django 2.2.7 on 2019-11-21 17:18

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone No')),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone No')),
                ('check_in_time', models.TimeField(auto_now=True, verbose_name='Check in time')),
                ('check_out_time', models.TimeField(verbose_name='Check out time')),
                ('address_visited', models.TextField(verbose_name='Address/Room Visited')),
                ('host_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='meeting.Host', verbose_name='Host Name')),
            ],
        ),
    ]
