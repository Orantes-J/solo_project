# Generated by Django 2.2 on 2021-04-12 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creations_app', '0014_auto_20210412_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(upload_to='creations_app/static/images'),
        ),
    ]