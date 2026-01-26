# from watchlist_app.models import Movie
# from watchlist_app.API.serializers import MovieSerializer
# from rest_framework.response import Response



# def movie_list(request):
#     movies=Movie.objects.all()
#     serializer=MovieSerializer(movies)
#     return Response(serializer.data)

# def movie_details(request,pk):
#     movie=Movie.objects.get(pk=pk)
#     serializer=MovieSerializer(movie)
#     return Response(serializer.data)