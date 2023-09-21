# Generated by Django 4.1.7 on 2023-09-13 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0005_notif'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_analyse', models.DateTimeField()),
                ('valeur_mesuree', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unite_mesure', models.CharField(max_length=50)),
                ('limite_detection', models.DecimalField(decimal_places=2, max_digits=10)),
                ('commentaire', models.TextField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('echantillon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.echantillon')),
                ('laboratoire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.laboratoire')),
                ('produit_angrais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.productengrais')),
                ('type_analyse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.typeanalyse')),
            ],
        ),
    ]