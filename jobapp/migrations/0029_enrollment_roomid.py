# Generated by Django 3.2.20 on 2024-01-24 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0028_course_seat'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='roomid',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]
