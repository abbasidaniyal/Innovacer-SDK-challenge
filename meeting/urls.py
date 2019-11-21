from django.urls import path
from meeting.views import HostUpdateView


urlpatterns = [
    path("/host-form", HostUpdateView.as_view(), name="host")
]
