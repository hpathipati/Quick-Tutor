# Generated by Django 3.0.3 on 2020-03-02 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0003_auto_20200224_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='rating',
        ),
    ]
