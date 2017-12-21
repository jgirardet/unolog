# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 10:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0003_patient_alive'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='LigneOrdonnance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField(unique=True)),
                ('ald', models.BooleanField(default=False)),
                ('object_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ordonnance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ordonnances', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordonnances', to='patients.Patient')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Conseil',
            fields=[
                ('ligneordonnance_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ordonnances.LigneOrdonnance')),
                ('contenu', models.TextField()),
            ],
            bases=('ordonnances.ligneordonnance',),
        ),
        migrations.CreateModel(
            name='Medicament',
            fields=[
                ('ligneordonnance_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ordonnances.LigneOrdonnance')),
                ('cip', models.CharField(max_length=20)),
                ('nom', models.CharField(max_length=200)),
                ('posologie', models.CharField(max_length=200)),
                ('duree', models.PositiveIntegerField()),
            ],
            bases=('ordonnances.ligneordonnance',),
        ),
        migrations.AddField(
            model_name='ligneordonnance',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='ligneordonnance',
            name='ordonnance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ligneordonnances', to='ordonnances.Ordonnance'),
        ),
    ]