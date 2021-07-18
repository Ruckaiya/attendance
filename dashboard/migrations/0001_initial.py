# Generated by Django 3.2.5 on 2021-07-17 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Class Name')),
                ('time', models.TimeField(verbose_name='Class Time')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(default='4ETT7vj9mgJZOPScOyYDUq2l3', max_length=100, verbose_name='Key')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Link Creation Time')),
                ('expiry', models.DateTimeField(verbose_name='Expiry Date Time')),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.class', verbose_name='Class')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(to='dashboard.Student', verbose_name='Students In This Class'),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_time', models.DateTimeField(auto_now_add=True, verbose_name='Attendance Time')),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.class', verbose_name='Class')),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.link')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.student', verbose_name='Students')),
            ],
        ),
    ]