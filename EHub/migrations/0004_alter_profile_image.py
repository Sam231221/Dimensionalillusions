# Generated by Django 3.2.7 on 2022-04-05 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EHub', '0003_rename_name_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
