# Generated by Django 2.2 on 2019-07-21 12:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('boardusers', '0431_auto_20190721_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 21, 12, 22, 36, 779700, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='users',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 21, 12, 22, 36, 779729, tzinfo=utc)),
        ),
    ]
