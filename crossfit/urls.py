from django.urls import path, include

from crossfit import views

urlpatterns = [
    path('', views.home, name='home'),
    path('workouts/', views.WorkoutListView.as_view(), name='workout_list'),
    path('workout/<int:pk>/', views.WorkoutDetailView.as_view(), name='workout_detail'),
    path('create-user/', views.UserCreateView.as_view(), name='create-user'),
    path('profile/<int:pk>', views.ProfileUpdateView.as_view(), name='profile-update'),

]
