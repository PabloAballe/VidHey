from django.db import models
from .utils.get_video_data_fun import *
from django.conf import settings

# Categories
class Categories(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_name=models.CharField(help_text='Category Name', max_length=255)
    category_desc=models.TextField(help_text='Category Description')
    created_at=models.DateTimeField(help_text='DateTime of creation', auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name

# PlayLists
class PlayLists(models.Model):
    playlist_id=models.AutoField(primary_key=True)
    playlist_name=models.CharField(help_text='PlayList Name', max_length=255)
    playlist_category=models.ForeignKey(Categories, on_delete=models.PROTECT)
    created_at=models.DateTimeField(help_text='DateTime of creation', auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "PlayList"
        verbose_name_plural = "PlayLists"
    
    def __str__(self):
        return self.playlist_name
# Videos
class Videos(models.Model):
    video_id=models.AutoField(primary_key=True)
    video_name=models.CharField(help_text='PlayList Name', max_length=255)
    video_desc=models.TextField(help_text='Video Description')
    video_yt_id=models.CharField(max_length=255, help_text='Video id from Youtube', unique=True)
    video_playlist=models.ForeignKey(PlayLists, on_delete=models.PROTECT)
    video_img=models.CharField(max_length=255)
    video_views=models.IntegerField(help_text='Number of visualizations of the video')
    video_published=models.BooleanField(default=True, help_text='Determine if the video is published')
    created_at=models.DateTimeField(help_text='DateTime of creation', auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Video"
        verbose_name_plural = "Videos"

    def __str__(self):
        return self.video_name
# Configuration
# YoutubeImporter
class YoutubeImporter(models.Model):
    yt_importer_id=models.AutoField(primary_key=True)
    yt_video_id=models.CharField(help_text='Video id from Youtube', max_length=1000)
    yt_video_playlist=models.ForeignKey(PlayLists, on_delete=models.CASCADE)
    created_at=models.DateTimeField(help_text='DateTime of creation', auto_now_add=True)

    def __str__(self):
        return self.yt_video_id

    def save(self, *args, **kwargs):
        video_data=get_video_data_fun(self.yt_video_id)
        Videos.objects.create(
           video_name=video_data["video_name"],
           video_desc=video_data["video_description"],
           video_yt_id=self.yt_video_id,
           video_playlist=self.yt_video_playlist,
           video_img=video_data["video_image"],
           video_views=0,
           video_published=True
        ).save()
        # super(YoutubeImporter, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "YoutubeImporter"
        verbose_name_plural = "YoutubeImporter"
    
    
# SavedVideos
class SavedVideos(models.Model):
    saved_video_id=models.AutoField(primary_key=True)
    saved_video_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )
    saved_video_category=models.ForeignKey(Categories, on_delete=models.CASCADE)
    saved_video_playlist=models.ForeignKey(PlayLists, on_delete=models.CASCADE)
    created_at=models.DateTimeField(help_text='DateTime of creation', auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "SavedVideo"
        verbose_name_plural = "SavedVideos"
    
    def __str__(self):
        return self.saved_video_id




