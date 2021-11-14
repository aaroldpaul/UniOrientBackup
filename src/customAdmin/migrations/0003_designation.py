# Generated by Django 3.2.9 on 2021-11-14 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customAdmin', '0002_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation_name', models.CharField(max_length=150, unique=True)),
                ('department_name', models.CharField(max_length=150)),
            ],
        ),
    ]
