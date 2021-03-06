# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcafeapp', '0041_auto_20150717_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bf_fruits_grains_menu',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='bf_morning_meals',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='bf_organic_eggs',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='bf_sandwitches',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='bf_sides',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='bf_sweets',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='dessertsmenu',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='kids_breakfast',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='kids_mains',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='kidsmenu_subcategories',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='lightmeals_subcategories',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='lm_salads',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='lm_sandwitches_burgers',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='lm_shareables',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='mains_grills_fromgrill',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='mains_grills_mains',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='mains_grills_sides',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='mainsgrills_subcategories',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='pizzamenu',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='ssj_bottled_juices',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='ssj_fresh_juices',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='ssj_milkshakes',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='ssj_smoothies',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='ssj_sparklers',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='ssj_subcategories',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='tea_coffees_cold_coffee',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='tea_coffees_hot_coffee',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='tea_coffees_tea',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='teacoffee_subcategories',
            name='cat_id',
        ),
        migrations.DeleteModel(
            name='BF_Fruits_Grains_Menu',
        ),
        migrations.DeleteModel(
            name='BF_Morning_Meals',
        ),
        migrations.DeleteModel(
            name='BF_Organic_Eggs',
        ),
        migrations.DeleteModel(
            name='BF_Sandwitches',
        ),
        migrations.DeleteModel(
            name='BF_Sides',
        ),
        migrations.DeleteModel(
            name='BF_Sweets',
        ),
        migrations.DeleteModel(
            name='DessertsMenu',
        ),
        migrations.DeleteModel(
            name='Kids_BreakFast',
        ),
        migrations.DeleteModel(
            name='Kids_Mains',
        ),
        migrations.DeleteModel(
            name='KidsMenu_SubCategories',
        ),
        migrations.DeleteModel(
            name='LightMeals_SubCategories',
        ),
        migrations.DeleteModel(
            name='LM_Salads',
        ),
        migrations.DeleteModel(
            name='LM_Sandwitches_Burgers',
        ),
        migrations.DeleteModel(
            name='LM_Shareables',
        ),
        migrations.DeleteModel(
            name='Mains_Grills_FromGrill',
        ),
        migrations.DeleteModel(
            name='Mains_Grills_Mains',
        ),
        migrations.DeleteModel(
            name='Mains_Grills_Sides',
        ),
        migrations.DeleteModel(
            name='MainsGrills_SubCategories',
        ),
        migrations.DeleteModel(
            name='PizzaMenu',
        ),
        migrations.DeleteModel(
            name='SSJ_Bottled_Juices',
        ),
        migrations.DeleteModel(
            name='SSJ_Fresh_Juices',
        ),
        migrations.DeleteModel(
            name='SSJ_MilkShakes',
        ),
        migrations.DeleteModel(
            name='SSJ_Smoothies',
        ),
        migrations.DeleteModel(
            name='SSJ_Sparklers',
        ),
        migrations.DeleteModel(
            name='SSJ_SubCategories',
        ),
        migrations.DeleteModel(
            name='Tea_Coffees_Cold_Coffee',
        ),
        migrations.DeleteModel(
            name='Tea_Coffees_Hot_Coffee',
        ),
        migrations.DeleteModel(
            name='Tea_Coffees_Tea',
        ),
        migrations.DeleteModel(
            name='TeaCoffee_SubCategories',
        ),
    ]
