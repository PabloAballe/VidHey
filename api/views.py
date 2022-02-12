from django.shortcuts import render
from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesModelSerializer
    filter_backends = [DjangoFilterBackend]

class PlayListsViewSet(viewsets.ModelViewSet):
    queryset = PlayLists.objects.all()
    serializer_class = PlayListsModelSerializer
    filter_backends = [DjangoFilterBackend]

class VideosViewSet(viewsets.ModelViewSet):
    queryset = Videos.objects.all()
    serializer_class = VideosModelSerializer
    filter_backends = [DjangoFilterBackend]

class SavedVideosViewSet(viewsets.ModelViewSet):
    queryset = SavedVideos.objects.all()
    serializer_class = SavedVideosModelSerializer
    filter_backends = [DjangoFilterBackend]