# Generated by Django 2.2 on 2021-04-12 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creations_app', '0010_auto_20210411_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(upload_to=''),
        ),
    ]
