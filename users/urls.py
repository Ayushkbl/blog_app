from django.urls import path
from . import views, apps

app_name = apps.UsersConfig.name
urlpatterns = [
    path('register/', views.register, name="register"),
    path('users/logout/', views.loggedout, name='do-logout'),
    path('profile/', views.profile, name="profile"),
]