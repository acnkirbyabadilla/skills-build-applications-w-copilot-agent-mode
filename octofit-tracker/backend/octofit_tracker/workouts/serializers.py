from rest_framework import serializers
from octofit_tracker.models import Workout

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'
