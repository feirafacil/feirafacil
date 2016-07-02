# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('cidade', models.CharField(max_length=50)),
                ('logradouro', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=30)),
                ('cidade', models.CharField(max_length=50)),
                ('logradouro', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('senha', models.CharField(max_length=9)),
                ('telefone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('myuser_ptr', models.OneToOneField(to='main.MyUser', auto_created=True, serialize=False, parent_link=True, primary_key=True)),
                ('zone', models.ForeignKey(to='main.Zone')),
            ],
            bases=('main.myuser',),
        ),
    ]
