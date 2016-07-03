# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160703_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='list_product',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='merchant',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
