# Generated by Django 5.0.4 on 2024-04-14 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crossfit', '0002_profile_age_profile_gender_profile_height_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='workoutresponse',
            name='weight_used',
            field=models.FloatField(blank=True, null=True),
        ),
    ]