# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcafeapp', '0037_auto_20150717_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordertrackingtable',
            name='sub_cat_id',
            field=models.IntegerField(null=True),
        ),
    ]
