# Generated by Django 5.0.4 on 2024-05-01 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_pet_created_at_pet_is_active_pet_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointment_type',
            field=models.CharField(choices=[('checkup', 'Check-Up'), ('vaccination', 'Vaccination'), ('6_month_wellness', '6 month Wellness'), ('surgery', 'Surgery'), ('dental', 'Dental'), ('other', 'Other')], default='checkup', max_length=50),
        ),
    ]