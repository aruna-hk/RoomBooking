# Generated by Django 4.2.16 on 2024-11-10 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='paid',
            field=models.TextField(choices=[('pending', 'pending'), ('paid', 'paid')], default='pending'),
        ),
    ]
