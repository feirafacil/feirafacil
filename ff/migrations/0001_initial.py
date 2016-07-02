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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('cidade', models.CharField(max_length=50)),
                ('logradouro', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('senha', models.CharField(max_length=9)),
                ('telefone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('myuser_ptr', models.OneToOneField(primary_key=True, parent_link=True, auto_created=True, to='ff.MyUser', serialize=False)),
                ('endereco', models.ForeignKey(to='ff.Address')),
            ],
            bases=('ff.myuser',),
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('myuser_ptr', models.OneToOneField(primary_key=True, parent_link=True, auto_created=True, to='ff.MyUser', serialize=False)),
                ('zone', models.ForeignKey(to='ff.Zone')),
            ],
            bases=('ff.myuser',),
        ),
    ]
