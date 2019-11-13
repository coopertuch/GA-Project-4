from django.db import models

class Workout(models.Model):
    name = models.CharField(max_length=100)
    muscle = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Lift(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='lifts')
    exercise = models.CharField(max_length=100, default='')
    reps = models.CharField(max_length=100, default='')
    weight = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.exercise