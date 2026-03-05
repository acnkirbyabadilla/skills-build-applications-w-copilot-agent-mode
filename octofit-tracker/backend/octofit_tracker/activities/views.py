from rest_framework import viewsets
from octofit_tracker.models import Activity
from .serializers import ActivitySerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
