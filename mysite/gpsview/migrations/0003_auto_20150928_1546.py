# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gpsview', '0002_auto_20150927_1942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coordinates',
            old_name='coordinate_date',
            new_name='coordinate_timestamp',
        ),
        migrations.AlterField(
            model_name='coordinates',
            name='lat',
            field=models.DecimalField(max_digits=10, decimal_places=7),
        ),
        migrations.AlterField(
            model_name='coordinates',
            name='lon',
            field=models.DecimalField(max_digits=10, decimal_places=7),
        ),
    ]
