# Generated by Django 2.0.7 on 2018-07-14 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('road', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='situation',
            name='endTime',
            field=models.DateTimeField(),
        ),
    ]
