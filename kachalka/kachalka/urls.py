from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registration/', views.registration, name='registration'),
    path('trains/', views.exercise_list, name='trains'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




