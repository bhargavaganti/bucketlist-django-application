# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 10:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BucketList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=b'', max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now_add=True)),
                ('is_public', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bucketlists', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date_modified',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BucketListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=b'', max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now_add=True)),
                ('done', models.BooleanField(default=False)),
                ('bucketlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='buppli.BucketList')),
            ],
            options={
                'ordering': ('date_modified',),
                'abstract': False,
            },
        ),
    ]