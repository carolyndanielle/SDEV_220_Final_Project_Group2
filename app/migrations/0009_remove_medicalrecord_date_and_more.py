# Generated by Django 5.0.4 on 2024-05-02 05:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_appointment_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalrecord',
            name='date',
        ),
        migrations.RemoveField(
            model_name='medicalrecord',
            name='diagnosis',
        ),
        migrations.RemoveField(
            model_name='medicalrecord',
            name='medication',
        ),
        migrations.RemoveField(
            model_name='medicalrecord',
            name='pet',
        ),
        migrations.RemoveField(
            model_name='medicalrecord',
            name='treatment',
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='document',
            field=models.FileField(default='', upload_to='medical_records/%Y/%m/%d/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
