# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('core', '0008_auto_20160521_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtUser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('email', models.EmailField(db_index=True, unique=True, max_length=255, verbose_name='Электронная почта')),
                ('avatar', models.ImageField(null=True, upload_to='user/avatar', blank=True, verbose_name='Аватар')),
                ('firstname', models.CharField(null=True, blank=True, max_length=40, verbose_name='Фамилия')),
                ('lastname', models.CharField(null=True, blank=True, max_length=40, verbose_name='Имя')),
                ('middlename', models.CharField(null=True, blank=True, max_length=40, verbose_name='Отчество')),
                ('date_of_birth', models.DateField(null=True, blank=True, verbose_name='Дата рождения')),
                ('register_date', models.DateField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Суперпользователь')),
                ('groups', models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', to='auth.Group', related_query_name='user', verbose_name='groups', blank=True)),
                ('user_permissions', models.ManyToManyField(help_text='Specific permissions for this user.', related_name='user_set', to='auth.Permission', related_query_name='user', verbose_name='user permissions', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Пользователи',
                'verbose_name': 'Пользователь',
            },
        ),
        migrations.RemoveField(
            model_name='mycustomemailuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='mycustomemailuser',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='MyCustomEmailUser',
        ),
    ]
