# Generated by Django 3.2.20 on 2024-01-23 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0023_alter_course_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
