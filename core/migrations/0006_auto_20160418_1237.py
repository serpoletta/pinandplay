# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20160418_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='info',
            field=models.TextField(blank=True),
        ),
    ]
