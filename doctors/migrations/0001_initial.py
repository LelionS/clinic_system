# Generated by Django 5.1.1 on 2024-09-16 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clock_number', models.CharField(max_length=50)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('relationship', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('test_type', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('diagnosis', models.TextField(blank=True, null=True)),
                ('prescription', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
