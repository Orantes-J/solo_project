# Generated by Django 2.2 on 2021-04-12 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creations_app', '0002_auto_20210407_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
