# Generated by Django 3.1.14 on 2022-05-19 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='username',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
