# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_name', models.CharField(max_length=128)),
                ('location_name', models.CharField(null=True, blank=True, max_length=128)),
                ('website', models.CharField(null=True, blank=True, max_length=128)),
                ('address1', models.CharField(blank=True, max_length=128)),
                ('address2', models.CharField(blank=True, max_length=128)),
                ('city', models.CharField(blank=True, max_length=128)),
                ('state', models.CharField(blank=True, max_length=128)),
                ('zipcode', models.CharField(blank=True, max_length=128)),
                ('contact', models.CharField(blank=True, max_length=128)),
                ('phone', models.CharField(blank=True, max_length=128)),
                ('hours', models.CharField(blank=True, max_length=1000)),
                ('category', models.ForeignKey(to='app.Category')),
            ],
        ),
    ]
