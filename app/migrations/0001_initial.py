# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=128)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('provider_name', models.CharField(max_length=128)),
                ('location_name', models.CharField(blank=True, null=True, max_length=128)),
                ('website', models.CharField(blank=True, null=True, max_length=128)),
                ('address1', models.CharField(blank=True, max_length=128)),
                ('address2', models.CharField(blank=True, max_length=128)),
                ('city', models.CharField(blank=True, max_length=128)),
                ('state', models.CharField(blank=True, max_length=128)),
                ('zipcode', models.CharField(blank=True, max_length=128)),
                ('contact', models.CharField(blank=True, max_length=128)),
                ('phone', models.CharField(blank=True, max_length=128)),
                ('hours', models.CharField(blank=True, max_length=128)),
                ('notes', models.CharField(blank=True, max_length=256)),
                ('category', models.ManyToManyField(blank=True, to='app.Category')),
            ],
        ),
    ]
