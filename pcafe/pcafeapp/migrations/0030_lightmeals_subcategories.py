# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcafeapp', '0029_breakfast_subcategories'),
    ]

    operations = [
        migrations.CreateModel(
            name='LightMeals_SubCategories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sub_cat_id', models.IntegerField()),
                ('subcat_name', models.CharField(max_length=50, null=True, blank=True)),
                ('cat_id', models.ForeignKey(to='pcafeapp.Categories')),
            ],
        ),
    ]
