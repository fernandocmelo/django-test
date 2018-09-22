from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Team(models.Model):
    id = models.IntegerField(primary_key=True)
    team_name = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.team_name

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    team_id = models.ForeignKey(Team,null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

class HappinessLevel(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    level = models.IntegerField(default=3)
    date = models.DateField(default=datetime.today().date())
