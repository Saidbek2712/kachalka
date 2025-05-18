from django.contrib import admin
from main.models import Clients
from .models import Exercise

admin.site.register(Clients)

admin.site.register(Exercise)