# Generated by Django 2.0.1 on 2018-01-09 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webscrapers', '0003_auto_20180109_0424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reddititem',
            old_name='api_ID',
            new_name='api_id',
        ),
    ]
