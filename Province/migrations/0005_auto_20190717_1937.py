# Generated by Django 2.2.3 on 2019-07-17 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Province', '0004_auto_20190717_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='province',
            name='featureImage',
            field=models.ImageField(blank=True, upload_to='media/images/provinces'),
        ),
    ]