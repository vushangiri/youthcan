# Generated by Django 3.0.8 on 2020-08-09 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_auto_20200809_1830'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='created_at',
            new_name='organized_at',
        ),
    ]