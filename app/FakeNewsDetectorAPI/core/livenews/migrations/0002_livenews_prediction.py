# Generated by Django 4.0.1 on 2023-08-26 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_livenews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livenews',
            name='prediction',
            field=models.BooleanField(default=True),
        ),
    ]