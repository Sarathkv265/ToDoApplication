# Generated by Django 5.0.7 on 2024-08-17 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='discription',
            field=models.TextField(null=True),
        ),
    ]
