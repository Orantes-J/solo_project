# Generated by Django 2.2 on 2021-04-13 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creations_app', '0017_auto_20210412_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='bio',
            field=models.TextField(),
        ),
    ]