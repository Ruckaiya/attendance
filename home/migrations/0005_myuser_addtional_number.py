# Generated by Django 3.2.5 on 2021-07-19 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210719_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='addtional_number',
            field=models.CharField(default=2, max_length=30, verbose_name='Addtional Phone Number'),
            preserve_default=False,
        ),
    ]