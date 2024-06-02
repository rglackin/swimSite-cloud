# Generated by Django 4.1.2 on 2022-11-14 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_swimmer_dob_alter_swimmer_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swimtime',
            name='distance',
            field=models.PositiveIntegerField(default=50, verbose_name='Distance'),
        ),
        migrations.AlterField(
            model_name='swimtime',
            name='time',
            field=models.DurationField(default=50, verbose_name='Time'),
        ),
    ]