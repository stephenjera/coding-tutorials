from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import RegistrationForm, ProfileEditForm, UserEditForm
from .models import WebsiteUser


def home(request):
    return render(request, "website/home.html")


@login_required
def profile(request):
    # Retrieve the logged-in user's details and display them
    user = request.user
    return render(request, "website/profile.html", {"user": user})


def site_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect("admin_users")
            else:
                return redirect("profile")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "website/login.html")


def site_logout(request):
    logout(request)
    return redirect("home")


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = RegistrationForm()
    return render(request, "website/register.html", {"form": form})


def profile_edit(request):
    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileEditForm(
            instance=request.user,
            initial={
                "date_of_birth": request.user.date_of_birth,
                "number": request.user.number,
                "cat_colour": request.user.cat_colour,
                "favourite_movie": request.user.favourite_movie,
            },
        )
    return render(request, "website/profile_edit.html", {"form": form})


def admin_users(request):
    users = WebsiteUser.objects.all()
    return render(request, "website/admin_users.html", {"users": users})


def admin_edit_user(request, user_id):
    user = WebsiteUser.objects.get(id=user_id)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("admin_users")
    else:
        form = UserEditForm(instance=user)
    return render(request, "website/admin_edit_user.html", {"user": user, "form": form})
