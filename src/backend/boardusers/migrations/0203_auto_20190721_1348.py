# Generated by Django 2.2 on 2019-07-21 05:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('boardusers', '0202_auto_20190721_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 21, 5, 47, 59, 599205, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='users',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 21, 5, 47, 59, 599241, tzinfo=utc)),
        ),
    ]
