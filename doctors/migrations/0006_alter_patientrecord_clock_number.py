# Generated by Django 5.1.1 on 2024-09-18 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0005_alter_patientrecord_clock_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientrecord',
            name='clock_number',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
