# Generated by Django 3.2.7 on 2022-03-25 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MArticles', '0011_rename_ip_address_visitior_ipaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='total_views',
            field=models.IntegerField(default=0),
        ),
    ]