# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='question',
            name='email',
            field=models.TextField(null=True, blank=True),
        ),
    ]
