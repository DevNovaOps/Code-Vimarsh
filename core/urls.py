"""
URLs for core app.
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('meet-the-team/', views.meet_team, name='meet_team'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('api/events/', views.events_api, name='events_api'),
    path('api/team/', views.team_api, name='team_api'),
]

