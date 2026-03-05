from django.urls import path
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def workouts_list(request):
    return Response({'message': 'Workouts endpoint works!'})

urlpatterns = [
    path('', workouts_list),
]
