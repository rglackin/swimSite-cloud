# Generated by Django 4.1.2 on 2022-12-14 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_competition_alter_swimtime_time_race'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='age_range',
            field=models.CharField(max_length=30),
        ),
    ]