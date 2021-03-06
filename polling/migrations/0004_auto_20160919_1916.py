# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-19 13:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polling', '0003_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalInsuranceSubjectData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DataOfReading', models.DateTimeField(blank=True, verbose_name='Date of Reading')),
                ('SugarMonitoringDeviceReading', models.FloatField(default=0)),
                ('WorkOutMachineDeviceReading', models.FloatField(default=0)),
                ('PulseMonitorReading', models.FloatField(default=0)),
                ('TemperatureMonitorReading', models.FloatField(default=0)),
                ('SleepPatternsMonitorReading', models.FloatField(default=0)),
                ('RegistrationID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='polling.HospitalSubjectRegistration')),
            ],
        ),
        migrations.RenameField(
            model_name='hospitalsubjectdeviceregistration',
            old_name='medical_history_brief',
            new_name='Patient_History',
        ),
        migrations.AddField(
            model_name='hospitalsubjectdeviceregistration',
            name='RegisterPatientRemoteMonitoring',
            field=models.NullBooleanField(),
        ),
    ]
