# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcafeapp', '0002_remove_contactus_pobox'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breakfastmenu',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='dessertsmenu',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='kids_meals',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='mains',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='pizzamenutable',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='sandwitches_burgers',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='sharables',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='sides',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='soups_salads_menu',
            name='cat_id',
        ),
        migrations.DeleteModel(
            name='BreakfastMenu',
        ),
        migrations.DeleteModel(
            name='DessertsMenu',
        ),
        migrations.DeleteModel(
            name='Kids_Meals',
        ),
        migrations.DeleteModel(
            name='Mains',
        ),
        migrations.DeleteModel(
            name='PizzaMenuTable',
        ),
        migrations.DeleteModel(
            name='Sandwitches_Burgers',
        ),
        migrations.DeleteModel(
            name='Sharables',
        ),
        migrations.DeleteModel(
            name='Sides',
        ),
        migrations.DeleteModel(
            name='Soups_Salads_Menu',
        ),
    ]
