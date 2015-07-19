# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcafeapp', '0039_auto_20150717_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items_Menu',
            fields=[
                ('item_id', models.AutoField(serialize=False, primary_key=True)),
                ('sub_cat_id', models.IntegerField()),
                ('item_name', models.CharField(max_length=50, null=True, blank=True)),
                ('ingrediants', models.CharField(default=b'', max_length=200)),
                ('price', models.CharField(max_length=25, null=True, blank=True)),
                ('cat_id', models.ForeignKey(to='pcafeapp.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategories',
            fields=[
                ('sub_cat_id', models.AutoField(serialize=False, primary_key=True)),
                ('sub_cat_name', models.CharField(max_length=50)),
                ('cat_id', models.ForeignKey(to='pcafeapp.Categories')),
            ],
        ),
        migrations.RemoveField(
            model_name='breakfast_subcategories',
            name='cat_id',
        ),
        migrations.DeleteModel(
            name='BreakFast_SubCategories',
        ),
    ]
