# Generated by Django 2.2.3 on 2019-07-17 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Province', '0002_auto_20190717_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='province',
            name='featureImage',
            field=models.ImageField(upload_to='province/'),
        ),
    ]