from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path("register/", views.register, name="register"),
    path("login/", views.site_login, name="login"),
    path("logout/", views.site_logout, name="logout"),
     path('users/', views.admin_users, name='admin_users'),
    path('edit-user/<int:user_id>/', views.admin_edit_user, name='admin_edit_user'),
]
