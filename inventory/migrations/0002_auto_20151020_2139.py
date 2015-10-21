# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='platform',
            name='family',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='platform',
            name='generation',
            field=models.IntegerField(default=0),
        ),
    ]
