# Generated by Django 2.1.2 on 2018-10-23 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0012_auto_20181022_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='audiofile',
            field=models.FileField(null=True, upload_to='audios/', verbose_name=''),
        ),
    ]
