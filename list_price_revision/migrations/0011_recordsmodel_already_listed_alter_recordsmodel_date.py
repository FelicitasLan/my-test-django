# Generated by Django 4.0 on 2021-12-16 16:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_price_revision', '0010_recordsmodel_remove_usermodel_records'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordsmodel',
            name='already_listed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='recordsmodel',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 17, 1, 44, 33, 989169), null=True),
        ),
    ]
