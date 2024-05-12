# Generated by Django 5.0.4 on 2024-05-10 04:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalMascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=10)),
                ('fecha_hora', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_vacuna', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duenio', models.CharField(max_length=10)),
                ('info_extra', models.TextField(blank=True, null=True)),
                ('fecha_de_nacimiento', models.DateField()),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appJeni.animalmascota')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialCita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_cita', models.TextField()),
                ('cita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appJeni.cita')),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appJeni.mascota')),
            ],
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raza', models.CharField(max_length=20, unique=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appJeni.animalmascota')),
            ],
        ),
        migrations.AddField(
            model_name='mascota',
            name='raza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appJeni.raza'),
        ),
        migrations.CreateModel(
            name='Vacunacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appJeni.mascota')),
                ('tipo_vacuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appJeni.vacuna')),
            ],
        ),
    ]