# Generated by Django 2.2.3 on 2019-08-14 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0003_auto_20190814_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='postal_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
