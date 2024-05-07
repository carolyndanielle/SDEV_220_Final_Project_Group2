# Generated by Django 5.0.4 on 2024-05-06 22:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_medicalrecord_user_medicalrecord_pet_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalrecord',
            name='uploaded_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]