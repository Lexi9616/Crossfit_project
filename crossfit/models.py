from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    gender = models.CharField(max_length=20),
    age = models.IntegerField(),
    height = models.IntegerField(),
    weight = models.FloatField(),
    # profile_pic = models.ImageField()

    def __str__(self):
        return self.get_full_name()


class Workout(models.Model):
    TYPE_CHOICES = [
        ('AMRAP', 'As Many Rounds As Possible'),
        ('EMOM', 'Every Minute On the Minute'),
        ('FOR_TIME', 'For Time'),
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.get_type_display()} - {self.date}"


class WorkoutResponse(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    time_taken = models.TimeField(blank=True, null=True)
    rounds_completed = models.IntegerField(blank=True, null=True)
    weight_used = models.FloatField()
