# Generated by Django 4.1.7 on 2023-09-21 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0009_moyenneanalyse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productanalyse',
            name='laborantins',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.laborantins'),
        ),
    ]
