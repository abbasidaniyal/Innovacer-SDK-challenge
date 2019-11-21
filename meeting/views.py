from django.shortcuts import render
from django.views.generic.edit import CreateView 

from meeting.models import Host, Guest
# from meeting.forms import HostForm, GuestForm


class HostCreateView(CreateView):
    # form_class = HostForm
    model = Host
    fields = ["name", "email", 'phone_no']
    # success_url=''
    # template_name = ".html"


class GuestCreateView(CreateView):


    model = Guest
    fields = ["name", "email", 'phone_no', "address_visited", 'host_name']
    # template_name = ".html"
