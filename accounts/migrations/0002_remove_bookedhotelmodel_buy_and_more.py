# Generated by Django 4.2.7 on 2024-01-22 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookedhotelmodel',
            name='buy',
        ),
        migrations.AddField(
            model_name='bookedhotelmodel',
            name='buy_status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('Accepted', 'Accepted')], default='PENDING', max_length=10),
        ),
    ]
