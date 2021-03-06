# Generated by Django 3.2.4 on 2021-06-13 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210610_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('fullTitle', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('image', models.CharField(max_length=100)),
                ('imDbRating', models.IntegerField()),
                ('imDbRatingCount', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('capacity', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
            ],
        ),
    ]
