from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# List of valid happiness values
HAPPINESS_LEVEL = [
    (1, 'Unhappy'),
    (2, 'Not Happy'),
    (3, 'Neutral'),
    (4, 'Happy'),
    (5, 'Very Happy'),
    ]

# Team Model
class Team(models.Model):
    """Defines the model to the team."""
    id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.team_name

# User Profile Model
class UserProfile(models.Model):
    """Defines the model to the user profile using django's users."""
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    team_id = models.ForeignKey(Team,null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

# Happiness Level Model
class HappinessLevel(models.Model):
    """Defines the model to register the UserProfile's happiness level."""
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    level = models.IntegerField(choices = HAPPINESS_LEVEL)
    date = models.DateField(default=datetime.today().date())
