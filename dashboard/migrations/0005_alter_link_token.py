# Generated by Django 3.2.5 on 2021-07-17 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20210718_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='token',
            field=models.CharField(default='908T2HAib7VqQDHvMj1eQlv07', editable=False, max_length=100, unique=True, verbose_name='Key'),
        ),
    ]
