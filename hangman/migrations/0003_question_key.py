# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-21 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0002_question_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='key',
            field=models.IntegerField(default=0),
        ),
    ]
