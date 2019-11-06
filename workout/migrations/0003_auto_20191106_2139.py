# Generated by Django 2.2.7 on 2019-11-06 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0002_auto_20191106_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lift',
            name='lift_type',
        ),
        migrations.RemoveField(
            model_name='lift',
            name='rep',
        ),
        migrations.AddField(
            model_name='lift',
            name='lift_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='lift',
            name='reps',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='lift',
            name='weight',
            field=models.CharField(default='', max_length=100),
        ),
    ]
