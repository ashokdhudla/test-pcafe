# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcafeapp', '0008_bf_organic_eggs'),
    ]

    operations = [
        migrations.CreateModel(
            name='BF_Sweets',
            fields=[
                ('bf_sw_id', models.AutoField(serialize=False, primary_key=True)),
                ('sub_cat_id', models.IntegerField()),
                ('sw_name', models.CharField(max_length=50, null=True, blank=True)),
                ('ingrediants', models.CharField(default=b'', max_length=200)),
                ('price', models.CharField(max_length=25, null=True, blank=True)),
                ('cat_id', models.ForeignKey(to='pcafeapp.Categories')),
            ],
        ),
    ]
