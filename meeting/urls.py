from django.urls import path
from meeting.views import HostCreateView,GuestCreateView,HomePage,GuestUpdateView
from django.shortcuts import render


urlpatterns = [
    path("", HomePage, name="home-page"),
    path("host-form/", HostCreateView.as_view(), name="host"),
    path("guest-form/", GuestCreateView.as_view(), name="guest"),
    path("guest-form-checkout/", GuestUpdateView.as_view(), name="guest-update"),
]
