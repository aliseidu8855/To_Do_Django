# Generated by Django 5.1.3 on 2024-11-29 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(default=''),
        ),
    ]