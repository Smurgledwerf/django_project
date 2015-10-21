# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('game_name', models.CharField(max_length=200)),
                ('hours_played', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('platform_name', models.CharField(max_length=100)),
                ('release_date', models.DateTimeField(verbose_name=b'date released')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='platform',
            field=models.ForeignKey(to='inventory.Platform'),
        ),
    ]
