from rest_framework import serializers
from .models import *

class CategoriesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class PlayListsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayLists
        fields = '__all__'

class VideosModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'

class SavedVideosModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedVideos
        fields = '__all__'