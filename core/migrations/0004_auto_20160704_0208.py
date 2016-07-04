# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_consumernotification_merchantnotification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consumer',
            old_name='name',
            new_name='username',
        ),
    ]
