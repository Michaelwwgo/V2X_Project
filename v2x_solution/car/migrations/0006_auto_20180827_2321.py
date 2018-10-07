# Generated by Django 2.0.7 on 2018-08-27 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_auto_20180818_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criminalcar',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='car.Car'),
        ),
        migrations.AlterField(
            model_name='criminalcar',
            name='creator',
            field=models.CharField(blank=True, default='', max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='criminalcar',
            name='location',
            field=models.CharField(blank=True, default='', max_length=140, null=True),
        ),
    ]