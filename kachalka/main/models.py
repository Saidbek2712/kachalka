from django.db import models

class Clients(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True)

    def __str__(self):
        return self.name

class MuscleGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    title = models.CharField(max_length=100)
    muscle_group = models.ForeignKey(MuscleGroup, on_delete=models.CASCADE, related_name='exercise')
    description = models.TextField()
    image = models.ImageField(upload_to='exercises', blank=True, null=True)

    def __str__(self):
        return self.title


