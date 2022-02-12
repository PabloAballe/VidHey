from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('/categories', views.CategoriesViewSet, basename='categories')
router.register('/playlists', views.PlayListsViewSet, basename='playlists')
router.register('/videos', views.VideosViewSet, basename='videos')
router.register('/saved-videos', views.SavedVideosViewSet, basename='saved-videos')

urlpatterns = [
    path('', include(router.urls))
]
