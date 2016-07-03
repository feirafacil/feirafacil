# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.AddField(
            model_name='consumer',
            name='telefone',
            field=models.CharField(default=123, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listproduct',
            name='consumer',
            field=models.ForeignKey(to='main.Consumer'),
        ),
        migrations.AddField(
            model_name='listproduct',
            name='products',
            field=models.ManyToManyField(to='main.Product'),
        ),
    ]
