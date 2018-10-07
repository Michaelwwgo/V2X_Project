# Generated by Django 2.0.7 on 2018-07-18 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('road', '0008_auto_20180717_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=140)),
                ('time', models.DateTimeField()),
                ('detail', models.CharField(max_length=140)),
                ('road', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='road.Road')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]