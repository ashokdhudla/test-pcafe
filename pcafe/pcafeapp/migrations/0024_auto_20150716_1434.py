# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcafeapp', '0023_tea_coffes_tea'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tea_Coffees_Cold_Coffee',
            fields=[
                ('cc_id', models.AutoField(serialize=False, primary_key=True)),
                ('sub_cat_id', models.IntegerField()),
                ('cc_name', models.CharField(max_length=50, null=True, blank=True)),
                ('ingrediants', models.CharField(default=b'', max_length=200)),
                ('price', models.CharField(max_length=25, null=True, blank=True)),
                ('cat_id', models.ForeignKey(to='pcafeapp.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Tea_Coffees_Hot_Coffee',
            fields=[
                ('hc_id', models.AutoField(serialize=False, primary_key=True)),
                ('sub_cat_id', models.IntegerField()),
                ('hc_name', models.CharField(max_length=50, null=True, blank=True)),
                ('ingrediants', models.CharField(default=b'', max_length=200)),
                ('price', models.CharField(max_length=25, null=True, blank=True)),
                ('cat_id', models.ForeignKey(to='pcafeapp.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Tea_Coffees_Tea',
            fields=[
                ('tea_id', models.AutoField(serialize=False, primary_key=True)),
                ('sub_cat_id', models.IntegerField()),
                ('tea_name', models.CharField(max_length=50, null=True, blank=True)),
                ('ingrediants', models.CharField(default=b'', max_length=200)),
                ('price', models.CharField(max_length=25, null=True, blank=True)),
                ('cat_id', models.ForeignKey(to='pcafeapp.Categories')),
            ],
        ),
        migrations.RemoveField(
            model_name='tea_coffes_cold_coffee',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='tea_coffes_hot_coffee',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='tea_coffes_tea',
            name='cat_id',
        ),
        migrations.DeleteModel(
            name='Tea_Coffes_Cold_Coffee',
        ),
        migrations.DeleteModel(
            name='Tea_Coffes_Hot_Coffee',
        ),
        migrations.DeleteModel(
            name='Tea_Coffes_Tea',
        ),
    ]
