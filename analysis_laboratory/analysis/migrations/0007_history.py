# Generated by Django 4.1.7 on 2023-09-13 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0006_resultat'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modification', models.DateTimeField(auto_now_add=True)),
                ('champ_modifie', models.CharField(max_length=255)),
                ('ancienne_valeur', models.CharField(max_length=255)),
                ('nouvelle_valeur', models.CharField(max_length=255)),
                ('laborantins', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.laborantins')),
                ('resultat_analyse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.resultat')),
            ],
            options={
                'verbose_name': "Historique d'Analyse",
                'verbose_name_plural': "Historiques d'Analyse",
            },
        ),
    ]
