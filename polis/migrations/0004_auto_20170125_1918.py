# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polis', '0003_auto_20170125_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shows',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
