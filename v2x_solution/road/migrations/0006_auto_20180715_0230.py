# Generated by Django 2.0.7 on 2018-07-14 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('road', '0005_auto_20180715_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='situation',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='situation',
            name='road',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='road.Road'),
        ),
    ]