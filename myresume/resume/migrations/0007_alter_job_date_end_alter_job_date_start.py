# Generated by Django 4.2.6 on 2023-10-23 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_alter_job_date_end_alter_job_date_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='date_end',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='job',
            name='date_start',
            field=models.CharField(max_length=30),
        ),
    ]