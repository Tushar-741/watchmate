from django.urls import path,include
# from watchlist_app.API.views import movie_list,movie_details
from watchlist_app.API.views import WatchListAV,WatchDetailAV,StreamPlatformAV,StreamPlatformDetailAV
urlpatterns = [
   path('stream/',StreamPlatformAV.as_view(),name='stream'),
   path('list/',WatchListAV.as_view(),name='movie-list'),
   path('<int:pk>',WatchDetailAV.as_view(),name='movie-detail'),
   path('stream/<int:pk>', StreamPlatformDetailAV.as_view(),name='stream-detail')
]