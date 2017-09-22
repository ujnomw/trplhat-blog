# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170918_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestFileContainer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('cont', models.FileField(upload_to='')),
            ],
        ),
    ]
