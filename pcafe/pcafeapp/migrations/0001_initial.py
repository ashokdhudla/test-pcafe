# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaDetails',
            fields=[
                ('areacode', models.IntegerField(serialize=False, primary_key=True)),
                ('areaname', models.CharField(default=b'', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BreakfastMenu',
            fields=[
                ('breakfast_id', models.AutoField(serialize=False, primary_key=True)),
                ('breakfast_name', models.CharField(max_length=25, null=True, blank=True)),
                ('ingrediants', models.CharField(default=b'', max_length=1000)),
                ('price', models.CharField(max_length=25)),
                ('item_code', models.CharField(default=b'', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('category_id', models.AutoField(serialize=False, primary_key=True)),
                ('category_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(default=0)),
                ('first_name', models.CharField(default=b'', max_length=50)),
                ('last_name', models.CharField(default=b'', max_length=50)),
                ('company', models.CharField(default=b'', max_length=50)),
                ('email', models.CharField(default=b'', max_length=100)),
                ('mobile', models.CharField(default=b'', max_length=15)),
                ('pobox', models.CharField(default=b'', max_length=10)),
                ('comments', models.CharField(default=b'', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='DessertsMenu',
            fields=[
                ('treat_id', models.AutoField(serialize=False, primary_key=True)),
                ('dessert_name', models.CharField(max_length=50, null=True, blank=True)),
                ('ingrediants', models.CharField(default=b'', max_length=200)),
                ('price', models.CharField(max_length=25, null=True, blank=True)),
                ('item_code', models.CharField(default=b'', max_length=30)),
                ('cat_id', models.ForeignKey(to='pcafeapp.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('feedbackid', models.AutoField(serialize=False, primary_key=True)),
                ('userid', models.IntegerField(default=0)),
                ('first_name', models.CharField(default=b'', max_length=50)),
                ('last_name', models.CharField(default=b'', max_length=50)),
                ('email', models.CharField(default=b'', max_length=50)),
                ('message', models.CharField(default=b'', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Kids_Meals',
            fields=[
                ('km_id', models.AutoField(serialize=False, primary_key=True)),
                ('km_name', models.CharField(default=b'', max_length=25)),
                ('ingrediants', models.CharField(default=b'', max_length=1000)),
                ('price', models.IntegerField()),
                ('item_code', models.CharField(default=b'', max_length=15)),
                ('cat_id', models.ForeignKey(to='pcafeapp.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Mains',
            fields=[
                ('main_id', models.AutoField(serialize=False, primary_key=True)),
                ('main_name', models.CharField(default=b'', max_length=25)),
                ('ingrediants', models.CharField(default=b'', max_length=1000)),
                ('price', models.IntegerField()),
                ('item_code', models.CharField(default=b'', max_length=15)),
                ('cat_id', models.ForeignKey(to='pcafeapp.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='OrderTrackingTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_id', models.IntegerField()),
                ('userid', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('item_id', models.IntegerField(null=True)),
                ('extras', models.CharField(max_length=200)),
                ('order_date', models.DateField(auto_now=True, max_length=25)),
                ('delivery_date', models.CharField(max_length=25, null=True)),
                ('choosen_items', models.CharField(max_length=100, blank=True)),
                ('cat_id', models.IntegerField(null=True)),
                ('order_type', models.CharField(default=b'yet_to_confirm', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaMenuTable',
            fields=[
                ('item_id', models.AutoField(serialize=False, primary_key=True)),
                ('item_name', models.CharField(max_length=50, null=True, blank=True)),
                ('ingrediants', models.CharField(default=b'', max_length=200)),
                ('price_small', models.CharField(max_length=25)),
                ('price_medium', models.CharField(max_length=25)),
                ('price_large', models.CharField(max_length=25)),
                ('item_code', models.CharField(max_length=30)),
                ('cat_id', models.ForeignKey(to='pcafeapp.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Sandwitches_Burgers',
            fields=[
                ('sb_id', models.AutoField(serialize=False, primary_key=True)),
                ('sb_name', models.CharField(default=b'', max_length=25)),
                ('ingrediants', models.CharField(default=b'', max_length=1000)),
                ('price', models.IntegerField()),
                ('item_code', models.CharField(default=b'', max_length=15)),
                ('cat_id', models.ForeignKey(to='pcafeapp.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Sharables',
            fields=[
                ('share_id', models.AutoField(serialize=False, primary_key=True)),
                ('share_name', models.CharField(default=b'', max_length=25)),
                ('ingrediants', models.CharField(default=b'', max_length=1000)),
                ('price', models.IntegerField()),
                ('item_code', models.CharField(default=b'', max_length=15)),
                ('cat_id', models.ForeignKey(to='pcafeapp.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Sides',
            fields=[
                ('side_id', models.AutoField(serialize=False, primary_key=True)),
                ('side_name', models.CharField(default=b'', max_length=25)),
                ('ingrediants', models.CharField(default=b'', max_length=1000)),
                ('price', models.IntegerField()),
                ('item_code', models.CharField(default=b'', max_length=15)),
                ('cat_id', models.ForeignKey(to='pcafeapp.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Soups_Salads_Menu',
            fields=[
                ('ss_id', models.AutoField(serialize=False, primary_key=True)),
                ('ss_name', models.CharField(max_length=50, null=True, blank=True)),
                ('ingrediants', models.CharField(default=b'', max_length=1000)),
                ('price', models.CharField(max_length=25, null=True, blank=True)),
                ('item_code', models.CharField(default=b'', max_length=15)),
                ('cat_id', models.ForeignKey(to='pcafeapp.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userid', models.IntegerField()),
                ('address', models.CharField(default=b'', max_length=100)),
                ('area', models.CharField(default=b'', max_length=50)),
                ('po_box', models.CharField(default=b'', max_length=40)),
                ('city', models.CharField(default=b'Dubai', max_length=30)),
                ('phone', models.CharField(default=b'', max_length=30)),
                ('is_primary', models.CharField(default=b'True', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('userid', models.AutoField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=50)),
                ('phone_no', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=25)),
                ('mobile', models.CharField(max_length=30)),
                ('how_abt_us', models.CharField(max_length=50)),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=0)),
                ('company', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='breakfastmenu',
            name='cat_id',
            field=models.ForeignKey(to='pcafeapp.Categories'),
        ),
    ]
