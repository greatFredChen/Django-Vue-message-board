# Generated by Django 2.2 on 2019-07-21 21:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('boardusers', '0962_auto_20190722_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 21, 21, 0, 15, 730190, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='users',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 21, 21, 0, 15, 730225, tzinfo=utc)),
        ),
    ]
