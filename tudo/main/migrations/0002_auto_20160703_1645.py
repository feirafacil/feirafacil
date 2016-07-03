# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consumer',
            old_name='logradouro',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='consumer',
            old_name='cidade',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='consumer',
            old_name='nome',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='consumer',
            old_name='numero',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='consumer',
            old_name='senha',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='consumer',
            old_name='telefone',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='merchant',
            old_name='senha',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='merchant',
            old_name='telefone',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='merchant',
            old_name='nome',
            new_name='username',
        ),
    ]
