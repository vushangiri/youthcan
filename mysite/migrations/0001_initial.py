# Generated by Django 3.0.8 on 2020-08-09 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('body_first', models.TextField(blank=True, null=True)),
                ('body_right', models.TextField(blank=True, null=True)),
                ('body_left', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'About',
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('facebook', models.URLField()),
                ('instagram', models.URLField()),
                ('youtube', models.URLField()),
                ('linkedin', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('logo', models.ImageField(upload_to='logo')),
            ],
            options={
                'verbose_name_plural': 'Base - Personal Data',
            },
        ),
        migrations.CreateModel(
            name='Advisors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='pics')),
                ('post', models.CharField(blank=True, max_length=50, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Base - Advisors',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saving_name', models.CharField(blank=True, default='Untitled', max_length=50, null=True)),
                ('body_left', models.TextField(blank=True, null=True)),
                ('body_right', models.TextField(blank=True, null=True)),
                ('body_center', models.TextField(blank=True, null=True)),
                ('body_quotes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateField()),
                ('brief_info', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='events')),
            ],
            options={
                'verbose_name_plural': 'Base - Events',
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('video_url', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Home - First',
            },
        ),
        migrations.CreateModel(
            name='HomeTitles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('home_our_work', models.CharField(max_length=200)),
                ('about_our_work', models.CharField(max_length=200)),
                ('event_description_our_work', models.CharField(max_length=200)),
                ('all_our_team', models.CharField(max_length=200)),
                ('all_our_advisors', models.CharField(max_length=200)),
                ('all_our_partners', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Base - Titles',
            },
        ),
        migrations.CreateModel(
            name='JoinUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('cv', models.FileField(upload_to='cv')),
            ],
            options={
                'verbose_name_plural': 'Base - JoinUs',
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='logo')),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Base - Partners',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('post', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='pics')),
                ('facebook', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Base - Team',
            },
        ),
        migrations.CreateModel(
            name='Values',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('photo_small', models.ImageField(blank=True, null=True, upload_to='values')),
                ('photo_big', models.ImageField(blank=True, null=True, upload_to='values')),
                ('body', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Home - Fourth',
            },
        ),
        migrations.CreateModel(
            name='Whatwedo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='whatwedo')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Home - Third',
            },
        ),
        migrations.CreateModel(
            name='Whoarewe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Home - Second',
            },
        ),
        migrations.CreateModel(
            name='Whoareweimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='whoarewe')),
                ('events', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mysite.Whoarewe')),
            ],
            options={
                'verbose_name_plural': 'Do not open - Whoareweimage',
            },
        ),
        migrations.CreateModel(
            name='Eventsgallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='events')),
                ('events', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mysite.Events')),
            ],
            options={
                'verbose_name_plural': 'Do not open - Eventgallaries',
            },
        ),
    ]
