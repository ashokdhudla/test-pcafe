# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcafeapp', '0048_auto_20150718_0643'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordertrackingtable',
            name='delivery_type',
            field=models.CharField(max_length=30, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ordertrackingtable',
            name='delivey_add',
            field=models.CharField(max_length=30, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ordertrackingtable',
            name='payment_method',
            field=models.CharField(max_length=30, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ordertrackingtable',
            name='special_req',
            field=models.CharField(max_length=80, blank=True),
            preserve_default=True,
        ),
    ]
