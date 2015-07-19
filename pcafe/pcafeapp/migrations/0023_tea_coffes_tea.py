# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcafeapp', '0022_tea_coffes_cold_coffee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tea_Coffes_Tea',
            fields=[
                ('tea_id', models.AutoField(serialize=False, primary_key=True)),
                ('sub_cat_id', models.IntegerField()),
                ('tea_name', models.CharField(max_length=50, null=True, blank=True)),
                ('ingrediants', models.CharField(default=b'', max_length=200)),
                ('price', models.CharField(max_length=25, null=True, blank=True)),
                ('cat_id', models.ForeignKey(to='pcafeapp.Categories')),
            ],
        ),
    ]
