# Generated by Django 4.0.3 on 2022-04-13 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classify', models.CharField(max_length=50)),
                ('age', models.IntegerField(max_length=50)),
                ('phenotype', models.IntegerField(max_length=200)),
                ('numbers', models.IntegerField()),
                ('size', models.IntegerField()),
                ('location', models.CharField(max_length=20)),
                ('migration', models.CharField(max_length=6)),
            ],
        ),
    ]
