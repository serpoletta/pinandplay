# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='extuser',
            name='username',
            field=models.CharField(max_length=40, blank=True, verbose_name='User name', null=True),
        ),
    ]
