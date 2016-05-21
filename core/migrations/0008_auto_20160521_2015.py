# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('core', '0007_auto_20160418_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCustomEmailUser',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('email', models.EmailField(max_length=255, verbose_name='email address', unique=True, db_index=True)),
                ('is_staff', models.BooleanField(verbose_name='staff status', help_text='Designates whether the user can log into this admin site.', default=False)),
                ('is_active', models.BooleanField(verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('date_of_birth', models.DateField()),
                ('groups', models.ManyToManyField(verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True, related_name='user_set', to='auth.Group', related_query_name='user')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', help_text='Specific permissions for this user.', blank=True, related_name='user_set', to='auth.Permission', related_query_name='user')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.AlterField(
            model_name='board',
            name='info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='link_to_game',
            field=models.URLField(max_length=300, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='picture',
            field=models.ImageField(upload_to='media/', blank=True, null=True),
        ),
    ]
