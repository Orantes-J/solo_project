# Generated by Django 2.2 on 2021-04-12 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creations_app', '0012_auto_20210412_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]