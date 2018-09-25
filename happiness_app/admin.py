from django.contrib import admin
from .models import UserProfile,Team,HappinessLevel

# Models that can be registered through django admin
admin.site.register(UserProfile)
admin.site.register(Team)
admin.site.register(HappinessLevel)
