from django import forms
from .models import HappinessLevel

# List of valid happiness values
HAPPINESS_LEVEL = [
    (1, 'Unhappy'),
    (2, 'Not Happy'),
    (3, 'Neutral'),
    (4, 'Happy'),
    (5, 'Very Happy'),
    ]

# Happiness Level Form
class HappinessLevelForm(forms.ModelForm):
    """Form class to register the happiness level of the user."""
    class Meta:
        model = HappinessLevel
        fields = (
            'level',
        )
        labels = {
            'level': ('Happiness Level'),
        }
