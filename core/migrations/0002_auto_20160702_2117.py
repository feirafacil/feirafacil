# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='MyUser',
        ),
        migrations.RenameField(
            model_name='consumer',
            old_name='user_ptr',
            new_name='myuser_ptr',
        ),
        migrations.RenameField(
            model_name='merchant',
            old_name='user_ptr',
            new_name='myuser_ptr',
        ),
    ]
