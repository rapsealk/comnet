# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-07 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0009_quiz_lives'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default', max_length=30)),
                ('number', models.IntegerField(default=0)),
                ('init', models.IntegerField(default=1)),
            ],
        ),
        migrations.AlterField(
            model_name='quiz',
            name='lives',
            field=models.IntegerField(default=8),
        ),
    ]