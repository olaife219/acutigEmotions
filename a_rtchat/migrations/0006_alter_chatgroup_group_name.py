# Generated by Django 5.1.1 on 2024-10-13 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_rtchat', '0005_groupmessage_file_alter_chatgroup_group_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatgroup',
            name='group_name',
            field=models.CharField(blank=True, max_length=128, unique=True),
        ),
    ]
