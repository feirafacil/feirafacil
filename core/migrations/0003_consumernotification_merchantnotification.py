# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160703_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumerNotification',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('message', models.TextField()),
                ('consumer', models.ForeignKey(to='core.Consumer')),
            ],
        ),
        migrations.CreateModel(
            name='MerchantNotification',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('message', models.TextField()),
                ('merchant', models.ForeignKey(to='core.Merchant')),
            ],
        ),
    ]
