# Generated by Django 4.0.3 on 2022-04-08 14:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pruefung',
            name='createTime',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='pruefung',
            name='updateTime',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime.now),
        ),
    ]