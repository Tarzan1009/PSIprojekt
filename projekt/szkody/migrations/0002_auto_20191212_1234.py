# Generated by Django 2.2.7 on 2019-12-12 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('szkody', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='PESEL',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='klient',
            name='PESEL',
            field=models.CharField(max_length=11),
        ),
    ]