# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20151020_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platform',
            name='family',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
