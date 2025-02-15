# Generated by Django 4.2.17 on 2024-12-21 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('posted_at', models.DateField()),
                ('updated_at', models.DateField()),
                ('location_type', models.JSONField(default=list)),
                ('compensation', models.JSONField(default=dict)),
                ('employment_type', models.JSONField(default=list)),
                ('skills', models.JSONField(default=list)),
                ('job_details', models.TextField()),
            ],
        ),
    ]
