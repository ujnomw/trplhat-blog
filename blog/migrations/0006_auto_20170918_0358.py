# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170918_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.FileField(upload_to='', null=True, blank=True),
        ),
    ]
