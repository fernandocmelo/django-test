from django import forms
from .models import HappinessLevel

HAPPINESS_LEVEL = [
    (1, 'Unhappy'),
    (2, 'Not Happy'),
    (3, 'Neutral'),
    (4, 'Happy'),
    (5, 'Very Happy'),
    ]

class HappinessLevelForm(forms.ModelForm):
    class Meta:
        model = HappinessLevel
        fields = ('level',)
        # happiness_level = forms.CharField(label='How are you feeling today?', widget=forms.RadioSelect(choices=HAPPINESS_LEVEL))
