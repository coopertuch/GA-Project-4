from django.db import models

class Workout(models.Model):
    muscle = models.CharField(max_length=100)

    def __str__(self):
        return self.type

class Lift(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='lifts')
    lift_type = models.CharField(max_length=100, default='no name')
    rep = models.CharField(max_length=100, default='no reps')
    weight = models.CharField(max_length=100, default='no weight')

    def __str__(self):
        return self.lift_type