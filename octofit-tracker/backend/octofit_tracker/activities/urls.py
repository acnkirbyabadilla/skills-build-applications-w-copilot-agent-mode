from django.urls import path
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def activities_list(request):
    return Response({'message': 'Activities endpoint works!'})

urlpatterns = [
    path('', activities_list),
]
