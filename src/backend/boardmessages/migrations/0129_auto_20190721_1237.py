# Generated by Django 2.2 on 2019-07-21 04:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('boardmessages', '0128_auto_20190721_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like_and_dislke',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 21, 4, 37, 23, 595771, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user_message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 21, 4, 37, 23, 594894, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user_message',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 21, 4, 37, 23, 594927, tzinfo=utc)),
        ),
    ]
