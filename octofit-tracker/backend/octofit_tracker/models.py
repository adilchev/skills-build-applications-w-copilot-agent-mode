from djongo import models
from bson import ObjectId

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    distance = models.FloatField()
    calories = models.IntegerField()
    def __str__(self):
        return f"{self.user.name} - {self.type}"

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='workouts')
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    def __str__(self):
        return f"{self.user.name} - {self.name}"

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboard')
    points = models.IntegerField()
    def __str__(self):
        return f"{self.team.name} - {self.points}"
