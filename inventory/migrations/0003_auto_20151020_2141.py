# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20151020_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platform',
            name='family',
            field=models.TextField(default=b'', max_length=100),
        ),
    ]
