from django import forms
from .models import Workout, Lift

class WorkoutForm(forms.ModelForm):

    class Meta:
        model = Workout
        fields = ('name', 'muscle',)

class LiftForm(forms.ModelForm):

    class Meta:
        model = Lift
        fields = ('exercise', 'reps', 'weight', 'workout',)