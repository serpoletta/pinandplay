# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('info', models.TextField(null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('is_private', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('picture', models.ImageField(null=True, upload_to='media/')),
                ('info', models.TextField(null=True)),
                ('last_edited_date', models.DateTimeField(auto_now=True)),
                ('link', models.URLField(max_length=300)),
                ('link_to_game', models.URLField(max_length=300)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('board', models.ForeignKey(to='core.Board')),
            ],
        ),
    ]
