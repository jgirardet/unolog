# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 08:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='observation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='observation',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='observation', to='patients.Patient'),
        ),
    ]
