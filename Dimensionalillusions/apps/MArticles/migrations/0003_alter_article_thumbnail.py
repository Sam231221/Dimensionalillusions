# Generated by Django 3.2.7 on 2021-11-13 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MArticles', '0002_auto_20211113_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.URLField(blank=True, null=True),
        ),
    ]
