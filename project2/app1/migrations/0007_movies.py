# Generated by Django 3.2.6 on 2021-08-12 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_employee_createdby'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mtitle', models.CharField(max_length=30)),
                ('hero', models.CharField(max_length=30)),
                ('heroin', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
