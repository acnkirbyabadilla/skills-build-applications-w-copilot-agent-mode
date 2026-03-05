from rest_framework import serializers
from octofit_tracker.models import Leaderboard

class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = '__all__'
