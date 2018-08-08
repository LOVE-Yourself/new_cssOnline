# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-11 18:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Active',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='新春活动', max_length=20, verbose_name='活动名称')),
                ('code', models.IntegerField(default=1, verbose_name='活动编号')),
                ('detail', models.TextField(verbose_name='活动规则')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '活动',
                'verbose_name_plural': '活动',
            },
        ),
        migrations.CreateModel(
            name='Advantage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=100, verbose_name='描述')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '课程优势',
                'verbose_name_plural': '课程优势',
            },
        ),
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='费用名称')),
                ('money', models.CharField(max_length=10, verbose_name='金额')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '费用明细',
                'verbose_name_plural': '费用明细',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='课程名称')),
                ('detail1', models.TextField(default='', verbose_name='费用详情')),
                ('detail2', models.TextField(default='', verbose_name='赠送课时')),
                ('cost_new', models.CharField(blank=True, default='4850', max_length=20, null=True, verbose_name='现价')),
                ('cost_old', models.CharField(blank=True, default='5000', max_length=20, null=True, verbose_name='原价')),
                ('image', models.ImageField(max_length=200, upload_to='course/%Y/%m', verbose_name='封面图')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
            },
        ),
        migrations.CreateModel(
            name='Practiceplace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='训练场地1', max_length=20, verbose_name='场地名称')),
                ('image', models.ImageField(upload_to='practicplace/%Y/%m', verbose_name='封面图')),
                ('detail', models.TextField(verbose_name='Tuobaba承诺')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '训练场地',
                'verbose_name_plural': '训练场地',
            },
        ),
        migrations.AddField(
            model_name='cost',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='相关课程'),
        ),
        migrations.AddField(
            model_name='advantage',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='课程'),
        ),
    ]
