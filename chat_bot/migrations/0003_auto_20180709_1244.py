# Generated by Django 2.0.7 on 2018-07-09 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_bot', '0002_auto_20170817_1641'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Objects_Content',
            new_name='ObjectsContent',
        ),
        migrations.RenameModel(
            old_name='Objects_Fields',
            new_name='ObjectsFields',
        ),
        migrations.RenameModel(
            old_name='Objects_Types',
            new_name='ObjectsTypes',
        ),
        migrations.RenameModel(
            old_name='User_Step',
            new_name='UserStep',
        ),
    ]
