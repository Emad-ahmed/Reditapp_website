# Generated by Django 3.2.6 on 2022-02-20 15:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reditapp', '0011_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 20, 21, 8, 34, 931296)),
        ),
    ]