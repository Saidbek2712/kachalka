from django.contrib import admin
from main.models import Clients
from .models import Exercise, MuscleGroup

admin.site.register(Clients)

admin.site.register(Exercise)

admin.site.register(MuscleGroup)

