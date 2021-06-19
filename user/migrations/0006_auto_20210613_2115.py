# Generated by Django 3.2.4 on 2021-06-13 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_events'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='fullTitle',
        ),
        migrations.RemoveField(
            model_name='events',
            name='imDbRating',
        ),
        migrations.RemoveField(
            model_name='events',
            name='imDbRatingCount',
        ),
        migrations.AlterField(
            model_name='events',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='events',
            name='image',
            field=models.CharField(max_length=800),
        ),
    ]