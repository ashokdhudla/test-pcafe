# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcafeapp', '0040_auto_20150717_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items_menu',
            name='sub_cat_id',
            field=models.ForeignKey(to='pcafeapp.SubCategories'),
        ),
    ]
