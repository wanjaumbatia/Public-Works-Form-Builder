# Generated by Django 5.0.6 on 2024-06-20 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_builder', '0010_field_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='required',
            field=models.BooleanField(default=False, verbose_name='Required'),
        ),
    ]
