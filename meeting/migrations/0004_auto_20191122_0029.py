# Generated by Django 2.2.7 on 2019-11-21 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0003_auto_20191122_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='check_out_time',
            field=models.TimeField(null=True, verbose_name='Check out time'),
        ),
    ]
