# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('email', models.EmailField(db_index=True, verbose_name='Email', unique=True, max_length=255)),
                ('avatar', models.ImageField(blank=True, verbose_name='Avatar image', upload_to='user/avatar', null=True)),
                ('firstname', models.CharField(blank=True, verbose_name='First name', null=True, max_length=40)),
                ('lastname', models.CharField(blank=True, verbose_name='Last name', null=True, max_length=40)),
                ('middlename', models.CharField(blank=True, verbose_name='Middle name', null=True, max_length=40)),
                ('date_of_birth', models.DateField(blank=True, verbose_name='Date of birth', null=True)),
                ('register_date', models.DateField(verbose_name='Registration date', auto_now_add=True)),
                ('is_active', models.BooleanField(verbose_name='Active', default=True)),
                ('is_admin', models.BooleanField(verbose_name='Is superuser', default=False)),
                ('groups', models.ManyToManyField(related_query_name='user', to='auth.Group', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True, related_name='user_set')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', to='auth.Permission', verbose_name='user permissions', help_text='Specific permissions for this user.', blank=True, related_name='user_set')),
            ],
            options={
                'verbose_name': 'user',
                'db_table': 'extuser',
                'verbose_name_plural': 'users',
            },
        ),
    ]
