# Generated by Django 5.1.1 on 2024-09-20 06:02

import doctors.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0008_patientrecord_unique_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientrecord',
            name='unique_code',
            field=models.CharField(default=doctors.models.generate_unique_code, max_length=12, unique=True),
        ),
    ]