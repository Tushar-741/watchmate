from django.urls import path,include
# from watchlist_app.API.views import movie_list,movie_details
from watchlist_app.API.views import WatchListAV,WatchDetailAV,StreamPlatformAV,StreamPlatformDetailAV,ReviewList,ReviewDetail

urlpatterns = [
   path('stream/',StreamPlatformAV.as_view(),name='stream'),
   path('list/',WatchListAV.as_view(),name='movie-list'),
   path('<int:pk>',WatchDetailAV.as_view(),name='movie-detail'),
   path('stream/<int:pk>', StreamPlatformDetailAV.as_view(),name='stream-detail'),
   
   path('review/', ReviewList.as_view(),name='review_list'),
   path('review/<int:pk>',ReviewDetail.as_view(),name='review-detail')
]