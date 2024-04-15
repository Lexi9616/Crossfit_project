from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, FormView

from crossfit.forms import UserForm, ProfileForm, WorkoutResponseForm
from crossfit.models import Workout, Profile, WorkoutResponse
from django import forms


class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user_id = self.request.user.pk
        profile = Profile.objects.get(id=current_user_id)
        context['profile'] = profile
        return context


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


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profileupdate.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.request.user.pk})

    def get_object(self, queryset=None):
        return self.request.user


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profiledetails.html'
    context_object_name = 'profile'


class AMRAPWorkoutResponseForm(forms.ModelForm):
    class Meta:
        model = WorkoutResponse
        fields = ['rounds_completed', 'weight_used']


class FOR_TIME_WorkoutResponseForm(forms.ModelForm):
    class Meta:
        model = WorkoutResponse
        fields = ['time_taken', 'weight_used']


class EMOMWorkoutResponseForm(forms.ModelForm):
    class Meta:
        model = WorkoutResponse
        fields = ['weight_used']


class SubmitWorkoutResponseView(LoginRequiredMixin, FormView):
    template_name = 'workout_response_form.html'

    def get_form_class(self):
        workout_id = self.kwargs['workout_id']
        workout = Workout.objects.get(pk=workout_id)
        if workout.type == 'AMRAP':
            return AMRAPWorkoutResponseForm
        elif workout.type == 'FOR_TIME':
            return FOR_TIME_WorkoutResponseForm
        elif workout.type == 'EMOM':
            return EMOMWorkoutResponseForm

    def form_valid(self, form):
        workout_id = self.kwargs['workout_id']
        workout = Workout.objects.get(pk=workout_id)
        response = form.save(commit=False)
        response.user = self.request.user
        response.workout = workout
        response.save()
        return redirect('workout_detail', pk=workout_id)
