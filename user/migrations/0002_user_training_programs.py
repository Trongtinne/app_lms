# Generated by Django 5.0.9 on 2024-09-22 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_program', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='training_programs',
            field=models.ManyToManyField(blank=True, to='training_program.trainingprogram'),
        ),
    ]
