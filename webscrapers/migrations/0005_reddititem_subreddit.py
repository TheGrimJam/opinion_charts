# Generated by Django 2.0.1 on 2018-01-09 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscrapers', '0004_auto_20180109_0437'),
    ]

    operations = [
        migrations.AddField(
            model_name='reddititem',
            name='subreddit',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]