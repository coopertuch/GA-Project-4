from django.urls import path
from . import views

urlpatterns = [
    path('', views.workout_list, name='workout_list'),
    path('lifts/', views.lift_list, name='lift_list'),
    path('workouts/<int:pk>', views.workout_detail, name='workout_detail'),
    path('lifts/<int:pk>', views.lift_detail, name='lift_detail'),
]