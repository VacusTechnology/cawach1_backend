# Generated by Django 3.1.6 on 2021-03-30 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastSeen', models.CharField(max_length=30)),
                ('inTime', models.CharField(max_length=30)),
                ('tagId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.asset')),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_1', models.CharField(max_length=2)),
                ('day_2', models.CharField(max_length=2)),
                ('day_3', models.CharField(max_length=2)),
                ('day_4', models.CharField(max_length=2)),
                ('day_5', models.CharField(max_length=2)),
                ('day_6', models.CharField(max_length=2)),
                ('day_7', models.CharField(max_length=2)),
                ('day_8', models.CharField(max_length=2)),
                ('day_9', models.CharField(max_length=2)),
                ('day_10', models.CharField(max_length=2)),
                ('day_11', models.CharField(max_length=2)),
                ('day_12', models.CharField(max_length=2)),
                ('day_13', models.CharField(max_length=2)),
                ('day_14', models.CharField(max_length=2)),
                ('day_15', models.CharField(max_length=2)),
                ('day_16', models.CharField(max_length=2)),
                ('day_17', models.CharField(max_length=2)),
                ('day_18', models.CharField(max_length=2)),
                ('day_19', models.CharField(max_length=2)),
                ('day_20', models.CharField(max_length=2)),
                ('day_21', models.CharField(max_length=2)),
                ('day_22', models.CharField(max_length=2)),
                ('day_23', models.CharField(max_length=2)),
                ('day_24', models.CharField(max_length=2)),
                ('day_25', models.CharField(max_length=2)),
                ('day_26', models.CharField(max_length=2)),
                ('day_27', models.CharField(max_length=2)),
                ('day_28', models.CharField(max_length=2)),
                ('day_29', models.CharField(max_length=2)),
                ('day_30', models.CharField(max_length=2)),
                ('day_31', models.CharField(max_length=2)),
                ('tagId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.asset')),
            ],
        ),
    ]
