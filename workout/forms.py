from django import forms
from .models import Workout, Lift

class WorkoutForm(forms.ModelForm):

    class Meta:
        model = Workout
        fields = ('muscle',)

class LiftForm(forms.ModelForm):

    class Meta:
        model = Lift
        fields = ('lift_name', 'reps', 'weight', 'workout',)