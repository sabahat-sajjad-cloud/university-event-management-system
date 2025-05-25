from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from functools import wraps

from .models import CustomUser


def custom_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Check if user is authenticated using YOUR session variable
        user_id = request.session.get("user_id")
        if user_id:
            # User is authenticated, proceed to the view
            return view_func(request, *args, **kwargs)
        else:
            # User is not authenticated, redirect to login page
            return redirect("login")

    return wrapper


@custom_login_required
def home(request):
    return render(request, "home.html")


@custom_login_required
def schedule(request):
    return render(request, "schedule.html")


@custom_login_required
def contact(request):
    return render(request, "contact.html")


@custom_login_required
def about(request):
    return render(request, "about.html")


@custom_login_required
def event(request):
    return render(request, "event.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = CustomUser.objects.get(username=username)
            if check_password(password, user.password):  # Verify hashed password
                request.session["user_id"] = user.id
                return redirect("home")
            else:
                return render(request, "login.html", {"error": "Invalid credentials."})
        except CustomUser.DoesNotExist:
            return render(request, "login.html", {"error": "Invalid credentials."})
    else:
        return render(request, "login.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        password = make_password(password)  # Hash the password
        
        # Create user object and save it
        user = CustomUser(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        user.save()

        return redirect("login")
    else:
        return render(request, "register.html")


def logout(request):
    # Clear all session data (logs out the user)
    request.session.flush()
    return redirect("login")

