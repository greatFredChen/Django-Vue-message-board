# Generated by Django 2.2 on 2019-07-21 06:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('boardmessages', '0240_auto_20190721_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like_and_dislke',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 21, 6, 59, 31, 631863, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user_message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 21, 6, 59, 31, 631208, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user_message',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 21, 6, 59, 31, 631233, tzinfo=utc)),
        ),
    ]
