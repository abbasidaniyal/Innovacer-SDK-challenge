# Generated by Django 2.2.7 on 2019-11-21 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0002_auto_20191122_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
    ]
