# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcafeapp', '0042_auto_20150717_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items_menu',
            name='cat_id',
            field=models.IntegerField(),
        ),
    ]
