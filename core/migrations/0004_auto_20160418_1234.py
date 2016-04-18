# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20160418_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='link_to_game',
            field=models.URLField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='picture',
            field=models.ImageField(upload_to='media/', blank=True),
        ),
    ]
