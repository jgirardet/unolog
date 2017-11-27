# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('street', models.CharField(blank=True, default='', max_length=200)),
                ('postalcode', models.CharField(blank=True, default='', max_length=5)),
                ('city', models.CharField(blank=True, default='', max_length=200)),
                ('phonenumber', models.CharField(blank=True, default='', max_length=20)),
                ('email', models.EmailField(blank=True, default='', max_length=100)),
            ],
        ),
    ]
