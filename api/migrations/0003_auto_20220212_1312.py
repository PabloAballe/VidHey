# Generated by Django 3.1.3 on 2022-02-12 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_youtubeimporter_yt_video_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='video_img',
            field=models.CharField(max_length=255),
        ),
    ]
