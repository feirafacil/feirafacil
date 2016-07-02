# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumer',
            name='endereco',
        ),
        migrations.AddField(
            model_name='consumer',
            name='cep',
            field=models.CharField(default=1, max_length=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consumer',
            name='cidade',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consumer',
            name='logradouro',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consumer',
            name='numero',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]
