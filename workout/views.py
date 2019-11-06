from django.shortcuts import render

from .models import Workout, Lift

def workout_list(request):
    workouts = Workout.objects.all()
    return render(request, 'workout/workout_list.html', {'workouts': workouts})

def lift_list(request):
    lifts = Lift.objects.all()
    return render(request, 'workout/lift_list.html', {'lifts': lifts})

def workout_detail(request, pk):
    workout = Workout.objects.get(id=pk)
    return render(request, 'workout/workout_detail.html', {'workout': workout})

def lift_detail(request, pk):
    lift = Lift.objects.get(id=pk)
    return render(request, 'workout/lift_detail.html', {'lift': lift})