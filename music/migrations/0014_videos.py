# Generated by Django 2.1.2 on 2018-10-23 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0013_songs_audiofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('videoid', models.AutoField(primary_key=True, serialize=False)),
                ('videotitle', models.CharField(max_length=100)),
                ('releasedate', models.DateField()),
                ('videofile', models.FileField(null=True, upload_to='audios/', verbose_name='')),
            ],
        ),
    ]
