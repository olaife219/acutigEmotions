# Generated by Django 5.1.1 on 2024-10-10 01:13

import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_rtchat', '0004_chatgroup_admin_chatgroup_groupchat_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmessage',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='chatgroup',
            name='group_name',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='groupmessage',
            name='body',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
