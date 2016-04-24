# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160414_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='labels',
            field=models.ManyToManyField(blank=True, to='core.Label'),
        ),
        migrations.AlterField(
            model_name='card',
            name='labels',
            field=models.ManyToManyField(blank=True, to='core.Label'),
        ),
    ]
