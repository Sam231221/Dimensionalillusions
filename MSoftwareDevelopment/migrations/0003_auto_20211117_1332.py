# Generated by Django 3.2.7 on 2021-11-17 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MSoftwareDevelopment', '0002_alter_framework_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='chapter_no',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13)], max_length=3, null=True, verbose_name='Chapter No'),
        ),
        migrations.AddField(
            model_name='topic',
            name='topic_no',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13)], max_length=3, null=True, verbose_name='Topic No'),
        ),
    ]
