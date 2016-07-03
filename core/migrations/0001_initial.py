# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='ListProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumer', models.ForeignKey(to='core.Consumer')),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=9)),
                ('phone', models.CharField(max_length=10)),
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
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('list_product', models.ForeignKey(to='core.ListProduct')),
                ('merchant', models.ForeignKey(to='core.Merchant')),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='merchant',
            name='zone',
            field=models.ForeignKey(to='core.Zone'),
        ),
        migrations.AddField(
            model_name='listproduct',
            name='products',
            field=models.ManyToManyField(to='core.Product'),
        ),
    ]
