# Generated by Django 4.1.3 on 2022-11-23 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_no', models.CharField(max_length=200, null=True)),
                ('model', models.CharField(blank=True, max_length=200)),
                ('color', models.CharField(max_length=200, null=True)),
                ('chasis_no', models.CharField(max_length=200, null=True)),
                ('engine_no', models.IntegerField(max_length=200, null=True)),
            ],
        ),
    ]
