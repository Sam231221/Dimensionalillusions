# Generated by Django 3.2.7 on 2021-10-31 05:09

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EHub', '0001_initial'),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='IpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenttype', models.CharField(default='Article', max_length=50)),
                ('visibility', models.CharField(choices=[('private', 'Private'), ('public', 'Public')], default='public', help_text="<p style='color:#b1b1b1;'>Private -> Only You can see this article.</p><p style='color:#b1b1b1;'>Public -> Anyone on the internet can see this article.</p>", max_length=20, verbose_name='type')),
                ('title', models.CharField(max_length=250, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='Articles/')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(help_text='Describe something.Dont repeat yourself.', null=True)),
                ('slug', models.SlugField(editable=False, null=True, unique=True)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('featured', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('bookmarks', models.ManyToManyField(blank=True, default=None, related_name='bookmarks', to='EHub.Profile')),
                ('category', models.ManyToManyField(blank=True, to='MArticles.Category')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('views', models.ManyToManyField(blank=True, related_name='post_views', to='MArticles.IpModel')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'db_table': 'article',
                'ordering': ('-published_date',),
            },
        ),
        migrations.CreateModel(
            name='AComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('commented_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='MArticles.article')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='MArticles.acomment')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Commentor', to='EHub.profile')),
            ],
            options={
                'ordering': ('-commented_on',),
            },
        ),
    ]