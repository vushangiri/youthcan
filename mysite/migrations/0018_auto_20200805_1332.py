# Generated by Django 3.0.8 on 2020-08-05 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0017_auto_20200805_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisors',
            name='post',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
