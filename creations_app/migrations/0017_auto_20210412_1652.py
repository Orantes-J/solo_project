# Generated by Django 2.2 on 2021-04-12 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creations_app', '0016_auto_20210412_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]