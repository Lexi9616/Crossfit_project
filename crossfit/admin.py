from django.contrib import admin

from .models import *

admin.site.register(Workout)
admin.site.register(Profile)
admin.site.register(WorkoutResponse)