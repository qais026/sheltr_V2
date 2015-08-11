# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('provider_name', models.CharField(max_length=128)),
                ('location_name', models.CharField(null=True, max_length=128, blank=True)),
                ('website', models.CharField(null=True, max_length=128, blank=True)),
                ('address1', models.CharField(max_length=128, blank=True)),
                ('address2', models.CharField(max_length=128, blank=True)),
                ('city', models.CharField(max_length=128, blank=True)),
                ('state', models.CharField(max_length=128, blank=True)),
                ('zipcode', models.CharField(max_length=128, blank=True)),
                ('contact', models.CharField(max_length=128, blank=True)),
                ('phone', models.CharField(max_length=128, blank=True)),
                ('hours', models.CharField(max_length=128, blank=True)),
                ('category', models.ForeignKey(to='app.Category')),
            ],
        ),
    ]
