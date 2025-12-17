from rest_framework import serializers
from .models import Team, UserProfile, Activity, Workout, Leaderboard

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['_id', 'name']

class UserProfileSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    team_id = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), source='team', write_only=True)
    class Meta:
        model = UserProfile
        fields = ['_id', 'email', 'name', 'team', 'team_id']

class ActivitySerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(), source='user', write_only=True)
    class Meta:
        model = Activity
        fields = ['_id', 'user', 'user_id', 'type', 'duration', 'distance', 'calories']

class WorkoutSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(), source='user', write_only=True)
    class Meta:
        model = Workout
        fields = ['_id', 'user', 'user_id', 'name', 'description', 'duration']

class LeaderboardSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    team_id = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), source='team', write_only=True)
    class Meta:
        model = Leaderboard
        fields = ['_id', 'team', 'team_id', 'points']
