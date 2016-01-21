# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('can_rock', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b"Member's name")),
                ('instrument', models.CharField(max_length=1, choices=[(b'g', b'Guitar'), (b'b', b'Bass'), (b'd', b'Drums'), (b'v', b'Vocal'), (b'p', b'Piano')])),
                ('band', models.ForeignKey(related_name=b'band', to='bands.Band')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
