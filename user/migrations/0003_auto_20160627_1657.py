# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20160627_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('description', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='consumer',
            name='author',
        ),
        migrations.RemoveField(
            model_name='consumer',
            name='text',
        ),
        migrations.RemoveField(
            model_name='consumer',
            name='title',
        ),
        migrations.RemoveField(
            model_name='merchant',
            name='author',
        ),
        migrations.RemoveField(
            model_name='merchant',
            name='text',
        ),
        migrations.RemoveField(
            model_name='merchant',
            name='title',
        ),
        migrations.AddField(
            model_name='consumer',
            name='address',
            field=models.ForeignKey(to='user.Address', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='merchant',
            name='zone',
            field=models.ForeignKey(to='user.Zone', default=1),
            preserve_default=False,
        ),
    ]
