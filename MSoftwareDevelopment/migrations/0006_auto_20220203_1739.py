# Generated by Django 3.2.7 on 2022-02-03 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSoftwareDevelopment', '0005_auto_20211117_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='views',
        ),
        migrations.DeleteModel(
            name='IpModel',
        ),
    ]
