# Generated by Django 4.1.7 on 2023-09-15 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0008_productanalyse_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoyenneAnalyse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moyenne', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('type_analyse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.typeanalyse')),
                ('type_produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.typeproduit')),
            ],
        ),
    ]
