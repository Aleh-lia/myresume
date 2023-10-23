# Generated by Django 4.2.6 on 2023-10-23 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_alter_university_date_end_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillfulness', models.CharField(max_length=100)),
                ('university_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.author')),
            ],
        ),
    ]
