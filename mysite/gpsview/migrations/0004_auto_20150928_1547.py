# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gpsview', '0003_auto_20150928_1546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coordinates',
            old_name='vehicle_id',
            new_name='vehicle',
        ),
    ]
