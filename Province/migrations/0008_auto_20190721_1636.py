# Generated by Django 2.2.3 on 2019-07-21 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Province', '0007_auto_20190718_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='province',
            name='englishName',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='mapUrl',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='sinhalaName',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='tamilName',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
