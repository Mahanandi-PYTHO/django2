# Generated by Django 3.2.6 on 2021-08-11 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=25)),
                ('branch', models.CharField(max_length=20)),
                ('roll_no', models.CharField(max_length=15)),
                ('college', models.CharField(max_length=30)),
                ('fees', models.IntegerField()),
                ('status', models.BooleanField(default=1)),
            ],
        ),
    ]