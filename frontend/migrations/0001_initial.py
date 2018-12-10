# Generated by Django 2.1.2 on 2018-12-10 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Affiliation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orgName', models.CharField(max_length=264, unique=True)),
                ('orgDetails', models.CharField(max_length=264)),
                ('orgImg', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='Recruiters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recName', models.CharField(max_length=264, unique=True)),
                ('recDetails', models.CharField(max_length=264)),
                ('recImg', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceName', models.CharField(max_length=264, unique=True)),
                ('imageUrl', models.CharField(max_length=264)),
                ('serviceText', models.CharField(max_length=264)),
            ],
        ),
    ]