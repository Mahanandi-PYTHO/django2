# Generated by Django 3.2.6 on 2021-08-13 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_movies_mimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='video',
            field=models.FileField(default='alt.mp4', upload_to='videos'),
        ),
    ]