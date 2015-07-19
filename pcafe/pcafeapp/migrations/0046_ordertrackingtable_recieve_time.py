# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pcafeapp', '0045_auto_20150717_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordertrackingtable',
            name='recieve_time',
            field=models.TimeField(default=datetime.time(0, 0), auto_now=True),
            preserve_default=False,
        ),
    ]
