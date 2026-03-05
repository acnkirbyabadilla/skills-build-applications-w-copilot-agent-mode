from django.urls import path
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def teams_list(request):
    return Response({'message': 'Teams endpoint works!'})

urlpatterns = [
    path('', teams_list),
]
