# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcafeapp', '0046_ordertrackingtable_recieve_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='verification_code',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
