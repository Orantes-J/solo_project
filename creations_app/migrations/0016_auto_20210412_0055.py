# Generated by Django 2.2 on 2021-04-12 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creations_app', '0015_auto_20210412_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
