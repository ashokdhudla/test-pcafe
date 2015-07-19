# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcafeapp', '0036_ssj_bottled_juices'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ssj_fresh_juices',
            old_name='sk_id',
            new_name='fj_id',
        ),
        migrations.RenameField(
            model_name='ssj_fresh_juices',
            old_name='sk_name',
            new_name='fj_name',
        ),
    ]
