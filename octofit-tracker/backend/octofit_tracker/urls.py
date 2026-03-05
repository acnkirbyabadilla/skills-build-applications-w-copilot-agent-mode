"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
import os

codespace_name = os.environ.get('CODESPACE_NAME')
codespace_host = f"{codespace_name}-8000.app.github.dev" if codespace_name else None
api_prefix = f"https://{codespace_host}/api/" if codespace_host else "/api/"


# DRF router for API root
from octofit_tracker.activities.views import ActivityViewSet
from octofit_tracker.users.views import UserViewSet
from octofit_tracker.teams.views import TeamViewSet
from octofit_tracker.leaderboard.views import LeaderboardViewSet
from octofit_tracker.workouts.views import WorkoutViewSet

router = DefaultRouter()
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'users', UserViewSet, basename='user')
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')
router.register(r'workouts', WorkoutViewSet, basename='workout')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/activities/', include('octofit_tracker.activities.urls')),
    path('api/users/', include('octofit_tracker.users.urls')),
    path('api/teams/', include('octofit_tracker.teams.urls')),
    path('api/leaderboard/', include('octofit_tracker.leaderboard.urls')),
    path('api/workouts/', include('octofit_tracker.workouts.urls')),
]
