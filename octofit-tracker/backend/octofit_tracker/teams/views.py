from rest_framework import viewsets
from octofit_tracker.models import Team
from .serializers import TeamSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
