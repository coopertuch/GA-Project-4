# Generated by Django 2.2.7 on 2019-11-13 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0004_workout_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lift',
            old_name='lift_name',
            new_name='exercise',
        ),
    ]