# Generated by Django 3.2.5 on 2021-07-19 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_myuser_is_completed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='is_verified',
            new_name='is_student',
        ),
    ]