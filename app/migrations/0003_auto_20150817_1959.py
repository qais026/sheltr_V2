# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provider',
            name='category',
        ),
        migrations.AddField(
            model_name='provider',
            name='category',
            field=models.ManyToManyField(to='app.Category'),
        ),
    ]
