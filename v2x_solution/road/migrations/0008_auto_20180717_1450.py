# Generated by Django 2.0.7 on 2018-07-17 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('road', '0007_auto_20180715_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='situation',
            name='creator',
            field=models.CharField(default='admin', max_length=140, null=True),
        ),
    ]