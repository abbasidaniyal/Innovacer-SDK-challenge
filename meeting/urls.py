from django.urls import path
from meeting.views import HostCreateView,GuestCreateView


urlpatterns = [
    path("/host-form", HostCreateView.as_view(), name="host"),
    path("/guest-form", GuestCreateView.as_view(), name="host"),
]
