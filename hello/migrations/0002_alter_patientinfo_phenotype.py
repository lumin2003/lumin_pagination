# Generated by Django 4.0.3 on 2022-04-13 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinfo',
            name='phenotype',
            field=models.CharField(max_length=200),
        ),
    ]
