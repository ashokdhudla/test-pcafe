# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcafeapp', '0014_mains_grills_mains'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mains_Grills_FromGrill',
            fields=[
                ('mg_fg_id', models.AutoField(serialize=False, primary_key=True)),
                ('sub_cat_id', models.IntegerField()),
                ('fg_name', models.CharField(max_length=50, null=True, blank=True)),
                ('ingrediants', models.CharField(default=b'', max_length=200)),
                ('price', models.CharField(max_length=25, null=True, blank=True)),
                ('cat_id', models.ForeignKey(to='pcafeapp.Categories')),
            ],
        ),
        migrations.RenameField(
            model_name='mains_grills_mains',
            old_name='lm_sb_id',
            new_name='mg_m_id',
        ),
    ]
