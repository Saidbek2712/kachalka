from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .models import Clients
from .models import Exercise, MuscleGroup

def main(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')

def login_view(request):
    return render(request, 'registration/login.html')

def exercise_list(request):

    group_id = request.GET.get('group')
    groups = MuscleGroup.objects.all()  # Все группы мышц

    if group_id:
        exercises = Exercise.objects.filter(muscle_group_id=group_id)
    else:
        exercises = Exercise.objects.all()

    return render(request, 'trains.html', {'exercises': exercises, 'groups': groups, 'request': request})

def registration(request):
    errors = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        email = request.POST.get('email')

        if not email:
            errors['email'] = 'Введите email.'
        elif User.objects.filter(email=email).exists():
            errors['email'] = 'Такая почта уже используется.'
        #сохранение данных пользователя если он регистрируется впервые
        if form.is_valid() and not errors:
            user = form.save(commit=False)
            user.email = email
            user.save()

            Clients.objects.create(name=user.username, email=email)
            auth_login(request, user)
            return redirect('login')

    else:
        form = UserCreationForm()

    return render(request, 'registration/registration.html', {'form': form, 'email_errors': errors})



