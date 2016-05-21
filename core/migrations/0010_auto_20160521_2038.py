# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20160521_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='extuser',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='ExtUser',
        ),
    ]
