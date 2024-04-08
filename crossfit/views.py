from django.shortcuts import render
from django.views.generic import ListView, DetailView

from crossfit.models import Workout, Profile


def home(request):
    return render(request, 'home.html')


class WorkoutListView(ListView):
    model = Workout
    template_name = 'wklist.html'
    context_object_name = 'workouts'


class WorkoutDetailView(DetailView):
    model = Workout
    template_name = 'wkdetails.html'
    context_object_name = 'workout'

