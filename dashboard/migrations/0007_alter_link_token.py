# Generated by Django 3.2.5 on 2021-07-17 23:43

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_link_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='token',
            field=models.CharField(default=dashboard.models.generate_key, max_length=100, unique=True, verbose_name='Key'),
        ),
    ]