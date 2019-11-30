# Generated by Django 2.2 on 2019-11-30 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='STCAClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=128)),
                ('bio_id', models.CharField(max_length=3000)),
                ('time_seed', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='STCATimedAuthenticationPerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_uri', models.CharField(max_length=200)),
                ('pair_key', models.CharField(max_length=64, unique=True)),
            ],
        ),
    ]