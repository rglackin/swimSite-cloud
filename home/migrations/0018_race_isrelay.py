# Generated by Django 4.1.2 on 2023-01-30 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_race_stroketype_alter_swimtime_stroketype'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='isRelay',
            field=models.BooleanField(default=False, verbose_name='Relay'),
        ),
    ]