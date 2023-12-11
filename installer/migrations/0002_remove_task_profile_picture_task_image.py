# Generated by Django 5.0 on 2023-12-10 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('installer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
