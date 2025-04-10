# Generated by Django 5.2 on 2025-04-10 03:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HealthProfessional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_name', models.CharField(max_length=255)),
                ('specialty', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='core.healthprofessional')),
            ],
        ),
    ]
