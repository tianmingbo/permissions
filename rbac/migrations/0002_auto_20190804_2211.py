# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-08-04 14:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roles',
            old_name='peimissions',
            new_name='permissions',
        ),
    ]
