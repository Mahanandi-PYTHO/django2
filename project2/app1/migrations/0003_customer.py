# Generated by Django 3.2.6 on 2021-08-11 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=20)),
                ('phone', models.BigIntegerField(max_length=15)),
                ('village', models.CharField(max_length=30)),
                ('order', models.IntegerField()),
                ('status', models.BooleanField(default=1)),
            ],
        ),
    ]
