# Generated by Django 2.2 on 2019-07-21 01:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('account', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2019, 7, 21, 1, 46, 24, 842734, tzinfo=utc))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2019, 7, 21, 1, 46, 24, 842761, tzinfo=utc))),
            ],
        ),
    ]
