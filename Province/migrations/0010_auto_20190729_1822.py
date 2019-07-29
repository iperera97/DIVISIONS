# Generated by Django 2.2.3 on 2019-07-29 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Province', '0009_auto_20190729_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='province',
            name='area',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='mapUrl',
            field=models.URLField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
