# Generated by Django 3.2.7 on 2022-02-03 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MArticles', '0007_alter_article_visibility'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='views',
        ),
        migrations.DeleteModel(
            name='IpModel',
        ),
    ]