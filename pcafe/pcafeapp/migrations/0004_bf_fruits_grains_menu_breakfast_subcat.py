# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcafeapp', '0003_auto_20150716_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='BF_Fruits_Grains_Menu',
            fields=[
                ('bf_fg_id', models.AutoField(serialize=False, primary_key=True)),
                ('fg_name', models.CharField(max_length=50, null=True, blank=True)),
                ('ingrediants', models.CharField(default=b'', max_length=200)),
                ('price', models.CharField(max_length=25, null=True, blank=True)),
                ('cat_id', models.ForeignKey(to='pcafeapp.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='BreakFast_SubCat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sub_cat_id', models.IntegerField()),
                ('Sub_cat_name', models.CharField(max_length=50)),
                ('cat_id', models.ForeignKey(to='pcafeapp.Categories')),
            ],
        ),
    ]
