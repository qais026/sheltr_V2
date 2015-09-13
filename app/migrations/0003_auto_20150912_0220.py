# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150912_0220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='provider',
            old_name='notes1',
            new_name='notes',
        ),
    ]
