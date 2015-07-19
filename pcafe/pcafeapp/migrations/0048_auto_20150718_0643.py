# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcafeapp', '0047_userdetails_verification_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='verification_code',
            field=models.CharField(max_length=10),
        ),
    ]
