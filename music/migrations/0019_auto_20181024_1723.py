# Generated by Django 2.1.2 on 2018-10-24 17:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0018_auto_20181024_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songdetails',
            name='songhits',
        ),
        migrations.AddField(
            model_name='songdetails',
            name='approved_comment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='songdetails',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='songdetails',
            name='text',
            field=models.TextField(null=True),
        ),
    ]