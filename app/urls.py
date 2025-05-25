from django.urls import path
from app.views import *
from . import views

urlpatterns = [
    path("", home, name="home"),
    path("home/", home, name="home"),
    path("schedule/", schedule, name="schedule"),
    path("contact-us/", contact, name="contact"),
    path("about-us/", about, name="contact"),
    path("event/", event, name="event"),
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout, name="logout"),
]
