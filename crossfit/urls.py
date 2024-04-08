from django.urls import path

from crossfit import views

urlpatterns = [
    path('', views.home, name='home'),
    path('workouts/', views.WorkoutListView.as_view(), name='workout_list'),
    path('workout/<int:pk>/', views.WorkoutDetailView.as_view(), name='workout_detail')
]
