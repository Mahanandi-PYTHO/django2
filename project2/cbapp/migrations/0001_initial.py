# Generated by Django 3.2.6 on 2021-08-20 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('skills', models.CharField(max_length=300)),
                ('roles', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=80)),
                ('logo', models.ImageField(default='alt.jpg', upload_to='media')),
            ],
        ),
    ]