# Generated by Django 2.2 on 2019-07-21 16:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('boardusers', '0791_auto_20190722_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 21, 16, 5, 36, 916632, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='users',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 21, 16, 5, 36, 916662, tzinfo=utc)),
        ),
    ]
