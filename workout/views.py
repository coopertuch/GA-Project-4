from django.shortcuts import render, redirect

from .forms import WorkoutForm

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

def workout_create(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save()
            return redirect('workout_detail', pk=workout.pk)
    else:
        form = WorkoutForm()
    return render(request, 'workout/workout_form.html', {'form': form})

from .forms import WorkoutForm, LiftForm

def lift_create(request):
    if request.method == 'POST':
        form = LiftForm(request.POST)
        if form.is_valid():
            lift = form.save()
            return redirect('lift_detail', pk=lift.pk)
    else:
        form = LiftForm()
    return render(request, 'workout/lift_form.html', {'form': form})

def workout_edit(request, pk):
    workout = Workout.objects.get(pk=pk)
    if request.method == "POST":
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            workout = form.save()
            return redirect('workout_detail', pk=workout.pk)
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'workout/workout_form.html', {'form': form})

def lift_edit(request, pk):
    lift = Lift.objects.get(pk=pk)
    if request.method == "POST":
        form = LiftForm(request.POST, instance=lift)
        if form.is_valid():
            workout = form.save()
            return redirect('lift_detail', pk=lift.pk)
    else:
        form = LiftForm(instance=lift)
    return render(request, 'workout/lift_form.html', {'form': form})

def workout_delete(request, pk):
    Workout.objects.get(id=pk).delete()
    return redirect('workout_list')

def lift_delete(request, pk):
    Lift.objects.get(id=pk).delete()
    return redirect('lift_list')