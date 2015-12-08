# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=128)),
                ('deadline', models.DateTimeField(auto_now_add=True)),
                ('requirement', models.TextField(default=b'', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=32)),
                ('note', models.TextField(default=b'', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=128)),
                ('location', models.CharField(default=b'', max_length=128)),
                ('note', models.TextField(default=b'', null=True)),
                ('component', models.ForeignKey(to='oven.Component')),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='contractor',
            field=models.ForeignKey(to='oven.Contractor'),
        ),
    ]
