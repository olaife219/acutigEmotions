from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile_view, name="profile"),
    path('edit/', views.profile_edit_view, name="profile-edit"),
    path('onboarding/', views.profile_edit_view, name="profile-onboarding"),
    path('settings/', views.profile_settings_view, name="profile-settings"),
    path('emailchange/', views.profile_emailchange, name="profile-emailchange"),
    path('emailverify/', views.profile_emailverify, name="profile-emailverify"),
    path('delete/', views.profile_delete_view, name="profile-delete"),
    path('dashboard/', views.dashboard, name='dashboard'),
]
