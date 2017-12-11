# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 06:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Journal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Journal.Topic')),
                # ('picture', models.FileField()),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]
