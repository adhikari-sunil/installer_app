# Generated by Django 5.0 on 2023-12-11 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('installer', '0003_alter_task_end_time_alter_task_start_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
