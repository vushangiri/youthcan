# Generated by Django 3.0.8 on 2020-08-09 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_auto_20200809_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='brief_info',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]