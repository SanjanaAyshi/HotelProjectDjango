# Generated by Django 4.2.7 on 2024-01-21 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('post', '0003_remove_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='categories.category'),
        ),
    ]
