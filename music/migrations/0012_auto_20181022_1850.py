# Generated by Django 2.1.2 on 2018-10-22 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_auto_20181022_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='albumlogo',
            field=models.ImageField(default='default.jpg', upload_to='_logo_pics'),
        ),
    ]