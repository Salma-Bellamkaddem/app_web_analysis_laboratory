# Generated by Django 4.1.7 on 2023-09-13 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0003_typeanalyse_typeproduit_productengrais'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAnalyse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultat', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_created', models.DateTimeField()),
                ('status', models.CharField(choices=[('encour', 'En cours'), ('realise', 'Réalisé')], default='encour', max_length=10)),
                ('laborantins', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='analysis.laborantins')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.location')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.productengrais')),
                ('type_analyse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.typeanalyse')),
                ('type_produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.typeproduit')),
            ],
        ),
    ]
