from django.urls import path
from meeting.views import *
from django.shortcuts import render


urlpatterns = [
    path(r"", HomePage, name="home-page"),
    # Add Authentication to create/update host
    path("host-form/", HostCreateView.as_view(), name="host"),
    path("guest-form/", GuestCreateView.as_view(), name="guest"),
    path("guest/<int:pk>/checkout/",
         GuestUpdateView.as_view(), name="guest-checkout"),
    # path('signup/', SignUp.as_view(), name="signup"),
]
