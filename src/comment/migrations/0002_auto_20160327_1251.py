# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 12:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created_at',), 'verbose_name': '\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439', 'verbose_name_plural': '\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438'},
        ),
    ]
