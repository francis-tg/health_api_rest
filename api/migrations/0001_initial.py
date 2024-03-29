# Generated by Django 5.0.1 on 2024-01-13 22:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maladie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=200)),
                ('num_tell', models.CharField(max_length=20)),
                ('ville', models.CharField(max_length=200)),
                ('centre', models.CharField(max_length=200)),
                ('date_naissance', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Prescriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('dosage', models.CharField(max_length=200)),
                ('id_patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Traitement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.patient')),
                ('id_prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.prescriptions')),
            ],
        ),
        migrations.CreateModel(
            name='EtatMaladie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
                ('id_maladie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.maladie')),
                ('id_traitement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.traitement')),
            ],
        ),
    ]
