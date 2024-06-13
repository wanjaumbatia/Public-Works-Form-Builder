# Generated by Django 5.0.6 on 2024-06-13 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_builder', '0006_field_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='field',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='fieldchoice',
            name='order',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
