# Generated by Django 3.0.8 on 2020-08-09 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0017_auto_20200809_2212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='body_left_image',
            new_name='left_image',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='body_right_image',
            new_name='right_image',
        ),
    ]
