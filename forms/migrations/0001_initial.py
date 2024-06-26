# Generated by Django 5.0.6 on 2024-06-16 13:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('forms_builder', '0008_alter_field_order_alter_fieldchoice_order'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_date', models.DateField(auto_now=True, verbose_name='Submission Date')),
                ('data', models.JSONField(verbose_name='Data')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='submissions', to='forms_builder.form')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'submission',
                'verbose_name_plural': 'submissions',
            },
        ),
    ]
