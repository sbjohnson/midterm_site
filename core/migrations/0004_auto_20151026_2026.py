# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151026_2020'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Question',
        ),
    ]
