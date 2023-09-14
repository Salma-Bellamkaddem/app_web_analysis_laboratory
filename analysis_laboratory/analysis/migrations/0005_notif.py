# Generated by Django 4.1.7 on 2023-09-13 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0004_productanalyse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('lue', models.BooleanField(default=True)),
                ('laborantins', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.laborantins')),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
                'ordering': ['-date_creation'],
            },
        ),
    ]
