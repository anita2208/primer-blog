# Generated by Django 3.2.25 on 2025-06-26 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20250622_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fotografía',
            name='opinion_personal',
        ),
    ]
