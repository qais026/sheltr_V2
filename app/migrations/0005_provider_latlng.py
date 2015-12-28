# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150921_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='latlng',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
