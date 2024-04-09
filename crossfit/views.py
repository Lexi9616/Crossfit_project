from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from crossfit.forms import UserForm
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


class UserCreateView(CreateView):
    form_class = UserForm
    success_url = reverse_lazy('home')
    model = Profile
    template_name = 'user_create.html'

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()

            return redirect('login')