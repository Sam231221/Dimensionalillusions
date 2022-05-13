# Generated by Django 3.2.7 on 2021-11-17 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MProgrammingLanguage', '0004_auto_20211117_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='chapter_no',
            field=models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13)], null=True, verbose_name='Chapter No'),
        ),
        migrations.AlterField(
            model_name='topics',
            name='topic_no',
            field=models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13)], null=True, verbose_name='Topic No'),
        ),
    ]
