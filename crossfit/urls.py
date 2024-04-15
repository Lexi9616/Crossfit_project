from django.urls import path, include

from crossfit import views
from crossfit.views import ProfileDetailView, SubmitWorkoutResponseView

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('workouts/', views.WorkoutListView.as_view(), name='workout_list'),
    path('workout/<int:pk>/', views.WorkoutDetailView.as_view(), name='workout_detail'),
    path('create-user/', views.UserCreateView.as_view(), name='create-user'),
    path('profile-details/<int:pk>/', ProfileDetailView.as_view(), name='profile-details'),
    path('profile-edit/<int:pk>', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('workout/<int:workout_id>/submit/', SubmitWorkoutResponseView.as_view(), name='submit_workout_response'),

]
