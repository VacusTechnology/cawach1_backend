# Generated by Django 3.1.6 on 2021-04-01 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyreport',
            name='inTime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='dailyreport',
            name='lastSeen',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
