# Generated by Django 2.0 on 2017-12-21 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordonnances', '0003_conseil_medicament'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ligneordonnance',
            name='position',
            field=models.PositiveIntegerField(),
        ),
    ]
