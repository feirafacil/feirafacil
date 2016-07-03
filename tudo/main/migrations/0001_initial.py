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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=10)),
                ('cidade', models.CharField(max_length=50)),
                ('logradouro', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='ListProduct',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('consumer', models.ForeignKey(to='main.Consumer')),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('senha', models.CharField(max_length=9)),
                ('telefone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('list_product', models.ForeignKey(to='main.ListProduct')),
                ('merchant', models.ForeignKey(to='main.Merchant')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('price', models.FloatField()),
                ('list_product', models.ForeignKey(to='main.ListProduct')),
                ('merchant', models.ForeignKey(to='main.Merchant')),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='merchant',
            name='zone',
            field=models.ForeignKey(to='main.Zone'),
        ),
        migrations.AddField(
            model_name='listproduct',
            name='products',
            field=models.ManyToManyField(to='main.Product'),
        ),
    ]
