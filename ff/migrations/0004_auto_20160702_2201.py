# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ff', '0003_auto_20160702_2155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumer',
            name='myuser_ptr',
        ),
        migrations.AddField(
            model_name='consumer',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consumer',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True, verbose_name='ID', default=1, auto_created=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consumer',
            name='nome',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consumer',
            name='senha',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
