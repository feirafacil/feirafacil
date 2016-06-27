# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=9)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='consumer',
            name='id',
        ),
        migrations.RemoveField(
            model_name='merchant',
            name='id',
        ),
        migrations.AddField(
            model_name='consumer',
            name='user_ptr',
            field=models.OneToOneField(to='user.User', serialize=False, default=1, parent_link=True, primary_key=True, auto_created=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='merchant',
            name='user_ptr',
            field=models.OneToOneField(to='user.User', serialize=False, default=1, parent_link=True, primary_key=True, auto_created=True),
            preserve_default=False,
        ),
    ]
