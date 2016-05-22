# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extuser', '0002_extuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extuser',
            name='is_admin',
            field=models.BooleanField(verbose_name='Is staff', default=False),
        ),
    ]
