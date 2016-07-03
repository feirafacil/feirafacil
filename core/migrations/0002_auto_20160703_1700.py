# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MerchantTender',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('price', models.FloatField()),
                ('list_product', models.ForeignKey(to='core.ListProduct')),
                ('merchant', models.ForeignKey(to='core.Merchant')),
            ],
        ),
        migrations.RemoveField(
            model_name='tender',
            name='list_product',
        ),
        migrations.RemoveField(
            model_name='tender',
            name='merchant',
        ),
        migrations.DeleteModel(
            name='Tender',
        ),
    ]
