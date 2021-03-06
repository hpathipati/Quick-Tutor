# Generated by Django 3.0.3 on 2020-04-17 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0009_auto_20200415_0548'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbr', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=50)),
                ('school', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='study.School')),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='subject',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='study.Subject'),
        ),
    ]
