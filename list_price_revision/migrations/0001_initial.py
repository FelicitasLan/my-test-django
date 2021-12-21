# Generated by Django 4.0 on 2021-12-15 09:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=1000)),
                ('q10_id', models.CharField(max_length=1000)),
                ('q10_password', models.CharField(max_length=1000)),
                ('description_header', models.TextField(default='')),
                ('description_footer', models.TextField(default='')),
                ('initial_letter', models.CharField(max_length=1)),
                ('delete_or_not', models.BooleanField(default=False)),
                ('shipping_code', models.CharField(default='', max_length=1000)),
                ('stock_num', models.IntegerField()),
                ('photo_num', models.IntegerField(default=3)),
                ('asin_list', models.TextField(default='')),
                ('group_black', models.TextField(default='')),
                ('maker_name_blacklist', models.TextField(default='')),
                ('asin_blacklist', models.TextField(default='')),
                ('words_blacklist', models.TextField(default='')),
                ('max_1', models.IntegerField(default=0)),
                ('max_2', models.IntegerField(default=0)),
                ('max_3', models.IntegerField(default=0)),
                ('rieki_1', models.IntegerField(default=0, max_length=3)),
                ('rieki_2', models.IntegerField(default=0, max_length=3)),
                ('rieki_3', models.IntegerField(default=0, max_length=3)),
                ('rieki_4', models.IntegerField(default=0, max_length=3)),
                ('kotei_1', models.IntegerField(default=0)),
                ('kotei_2', models.IntegerField(default=0)),
                ('kotei_3', models.IntegerField(default=0)),
                ('kotei_4', models.IntegerField(default=0)),
                ('kaitei_kankaku', models.TimeField(default=datetime.time(2, 0))),
            ],
        ),
    ]
