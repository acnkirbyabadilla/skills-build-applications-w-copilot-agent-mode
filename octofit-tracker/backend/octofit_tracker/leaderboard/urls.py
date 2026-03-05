from django.urls import path
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def leaderboard_list(request):
    return Response({'message': 'Leaderboard endpoint works!'})

urlpatterns = [
    path('', leaderboard_list),
]
