# Generated by Django 3.1.6 on 2021-03-30 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gateway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gatewayId', models.CharField(max_length=40, unique=True)),
                ('gatewayName', models.CharField(max_length=30)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
