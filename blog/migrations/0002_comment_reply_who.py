# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-13 03:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='reply_who',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='回复谁'),
        ),
    ]