# Generated by Django 2.2 on 2019-07-21 15:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('boardmessages', '0674_auto_20190721_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like_and_dislke',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 21, 15, 35, 39, 659836, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user_message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 21, 15, 35, 39, 658909, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user_message',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 21, 15, 35, 39, 658950, tzinfo=utc)),
        ),
    ]
