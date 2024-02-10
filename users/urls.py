from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/<int:pk>/update', views.profile_update, name='profile_update'),

    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
]