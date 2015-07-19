# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcafeapp', '0034_ssj_subcategories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mains_grills_mains',
            old_name='sb_name',
            new_name='main_name',
        ),
    ]
