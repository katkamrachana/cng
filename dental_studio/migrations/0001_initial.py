# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-16 05:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appt_datetime', models.DateTimeField()),
                ('appt_by_name', models.CharField(max_length=50, unique=True)),
                ('appt_contact', models.CharField(max_length=12, unique=True)),
                ('appt_email', models.EmailField(max_length=50, unique=True)),
                ('appt_address', models.CharField(max_length=300)),
                ('appt_age', models.IntegerField(default=0)),
                ('appt_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_fname', models.CharField(max_length=30, unique=True)),
                ('patient_lname', models.CharField(max_length=30, unique=True)),
                ('patient_contact', models.CharField(max_length=12, unique=True)),
                ('patient_email', models.EmailField(max_length=50, unique=True)),
                ('patient_address', models.CharField(max_length=300)),
                ('patient_age', models.IntegerField(default=0)),
                ('first_appt_date', models.DateTimeField(verbose_name='date joined')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=2000)),
                ('created_date', models.DateTimeField()),
                ('user', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment_name', models.CharField(max_length=200, unique=True)),
                ('treatment_description', models.CharField(max_length=500)),
                ('treatment_cost', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visited_date', models.DateTimeField()),
                ('comments', models.CharField(max_length=2000)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dental_studio.Appointment')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dental_studio.Patient')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dental_studio.Treatment')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='treatment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dental_studio.Treatment'),
        ),
    ]