# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20150520_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featurepagefeatureaspect',
            name='feature_aspect',
            field=models.ForeignKey(to='core.FeatureAspect', related_name='+'),
            preserve_default=True,
        ),
    ]
