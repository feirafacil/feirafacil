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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('cidade', models.CharField(max_length=50)),
                ('logradouro', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('senha', models.CharField(max_length=9)),
                ('telefone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, serialize=False, primary_key=True, auto_created=True, to='core.User')),
                ('endereco', models.ForeignKey(to='core.Address')),
            ],
            bases=('core.user',),
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, serialize=False, primary_key=True, auto_created=True, to='core.User')),
                ('zone', models.ForeignKey(to='core.Zone')),
            ],
            bases=('core.user',),
        ),
    ]
