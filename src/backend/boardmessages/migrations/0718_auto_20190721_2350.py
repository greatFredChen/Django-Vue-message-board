# Generated by Django 2.2 on 2019-07-21 15:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('boardmessages', '0717_auto_20190721_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like_and_dislke',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 21, 15, 50, 8, 503573, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user_message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 21, 15, 50, 8, 501200, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user_message',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 21, 15, 50, 8, 501241, tzinfo=utc)),
        ),
    ]
