# Generated by Django 5.1.1 on 2024-09-21 03:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('full_name', models.CharField(editable=False, max_length=511)),
                ('class_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='class.classinfo')),
            ],
        ),
    ]
