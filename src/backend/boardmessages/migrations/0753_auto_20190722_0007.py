# Generated by Django 2.2 on 2019-07-21 16:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('boardmessages', '0752_auto_20190722_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like_and_dislke',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 21, 16, 7, 49, 895628, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user_message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 21, 16, 7, 49, 895138, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user_message',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 21, 16, 7, 49, 895195, tzinfo=utc)),
        ),
    ]
