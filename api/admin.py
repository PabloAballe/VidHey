from django.contrib import admin
from .models import *

class CategoriesAdmin(admin.ModelAdmin):
    list_filter = ('created_at',)
    search_fields = ("category_name",)

class PlayListsAdmin(admin.ModelAdmin):
    list_filter = ('created_at',)
    search_fields = ("playlist_name",)

class VideosAdmin(admin.ModelAdmin):
    list_filter = ('created_at',)
    search_fields = ("video_name",)

class YoutubeImporterAdmin(admin.ModelAdmin):
    list_filter = ('created_at',)
    search_fields = ("yt_video_id",)

class SavedVideosAdmin(admin.ModelAdmin):
    list_filter = ('saved_video_user','created_at', 'saved_video_category', 'saved_video_playlist', )
    search_fields = ("url",)


# Register your models here.
admin.site.register(Categories,CategoriesAdmin )
admin.site.register(PlayLists, PlayListsAdmin)
admin.site.register(Videos, VideosAdmin)
admin.site.register(YoutubeImporter, YoutubeImporterAdmin)
admin.site.register(SavedVideos, SavedVideosAdmin)