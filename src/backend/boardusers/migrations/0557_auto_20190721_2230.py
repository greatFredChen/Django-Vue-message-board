# Generated by Django 2.2 on 2019-07-21 14:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('boardusers', '0556_auto_20190721_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 21, 14, 30, 19, 830665, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='users',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 21, 14, 30, 19, 830705, tzinfo=utc)),
        ),
    ]
