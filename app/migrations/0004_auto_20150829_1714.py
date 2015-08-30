# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150817_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='category',
            field=models.ManyToManyField(to='app.Category', blank=True),
        ),
    ]
