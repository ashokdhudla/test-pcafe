# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcafeapp', '0024_auto_20150716_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='SSJ_Smoothies',
            fields=[
                ('smoothie_id', models.AutoField(serialize=False, primary_key=True)),
                ('sub_cat_id', models.IntegerField()),
                ('smoothie_name', models.CharField(max_length=50, null=True, blank=True)),
                ('ingrediants', models.CharField(default=b'', max_length=200)),
                ('price', models.CharField(max_length=25, null=True, blank=True)),
                ('cat_id', models.ForeignKey(to='pcafeapp.Categories')),
            ],
        ),
    ]
