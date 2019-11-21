from django.shortcuts import render
from django.views import CreateView

from meeting.models import Host, Guest
from meeting.forms import HostForm, GuestForm


class HostUpdateView(CreateView):
    # form_class = HostForm
    model = Host
    fields = ["name", "email", 'phone_no']
    # success_url=''
    # template_name = ".html"


class GuestUpdateView(CreateView):
    # form_class = GuestForm
    # success_url=''

    model = Guest
    fields = ["name", "email", 'phone_no', "address_visited", 'host_name']
    # template_name = ".html"
