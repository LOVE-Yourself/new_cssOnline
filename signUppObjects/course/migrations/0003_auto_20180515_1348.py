# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-15 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_practiceplace'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='discount',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='优惠金额'),
        ),
        migrations.AddField(
            model_name='course',
            name='pay_mount',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='支付金额'),
        ),
    ]
