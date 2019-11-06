from django.urls import path
from . import views

urlpatterns = [
    path('', views.workout_list, name='workout_list'),
    path('lifts/', views.lift_list, name='lift_list'),
    path('workouts/<int:pk>', views.workout_detail, name='workout_detail'),
    path('lifts/<int:pk>', views.lift_detail, name='lift_detail'),
    path('workouts/new', views.workout_create, name='workout_create'),
    path('lifts/new', views.lift_create, name='lift_create'),
    path('workouts/<int:pk>/edit', views.workout_edit, name='workout_edit'),
    path('lifts/<int:pk>/edit', views.lift_edit, name='lift_edit'),
    path('workouts/<int:pk>/delete', views.workout_delete, name='workout_delete'),
    path('lifts/<int:pk>/delete', views.lift_delete, name='lift_delete')
]