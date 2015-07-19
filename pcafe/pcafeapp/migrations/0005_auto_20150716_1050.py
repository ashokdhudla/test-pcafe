# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcafeapp', '0004_bf_fruits_grains_menu_breakfast_subcat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breakfast_subcat',
            name='cat_id',
        ),
        migrations.AddField(
            model_name='bf_fruits_grains_menu',
            name='sub_cat_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='BreakFast_SubCat',
        ),
    ]
