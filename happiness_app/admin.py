from django.contrib import admin
from .models import UserProfile,Team,HappinessLevel

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Team)
admin.site.register(HappinessLevel)
