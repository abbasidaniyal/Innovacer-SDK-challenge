from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils import timezone

from meeting.models import Host, Guest
from meeting.forms import HostForm, GuestForm, GuestFormCheckout


def HomePage(request):
    return render(request, "meeting/index.html",)


class HostCreateView(CreateView):

    '''
    HostCreateView is used to create a new host. Since this requires security, only super admins can use this functionality.
    '''
    model = Host
    form_class = HostForm
    success_url = reverse_lazy("home-page")

    def form_valid(self, form):
        super(HostCreateView, self).form_valid(form)

        messages.success(self.request, 'Host Added successfully!')
        return HttpResponseRedirect(self.get_success_url())


class HostUpdateView(UpdateView):
    '''
    HostUpdateView is used to update the Host. It also sends an email to the Host about his details. 
    '''
    model = Host
    form_class = HostForm
    success_url = reverse_lazy("home-page")
    # template_name = 'meeting/host_.html'

    def form_valid(self, form):
        # setting the checkout time to current time

        super(HostUpdateView, self).form_valid(form)
        messages.success(self.request, 'Host Edited successfully!')
        form.send_mail_to_Host()

        return HttpResponseRedirect(self.get_success_url())


class GuestCreateView(CreateView):
    '''
    GuestCreateView is used to create a new guest and notify his host via SMS/Email about the details of his guest
    '''
    model = Guest
    form_class = GuestForm
    success_url = reverse_lazy("home-page")

    def form_valid(self, form):
        super(GuestCreateView, self).form_valid(form)
        messages.success(self.request, 'Guest Added successfully!')
        form.send_sms_to_host()
        form.send_mail_to_host()
        return HttpResponseRedirect(self.get_success_url())


class GuestUpdateView(UpdateView):
    '''
    GuestUpdateView is used to update the checkout time of the Guest. It also sends an email to the Guest about his details,Host Details etc 
    '''
    model = Guest
    form_class = GuestFormCheckout
    success_url = reverse_lazy("home-page")
    template_name = 'meeting/guest_checkout.html'

    def form_valid(self, form):
        # setting the checkout time to current time
        self.object.check_out_time = timezone.now()

        super(GuestUpdateView, self).form_valid(form)
        messages.success(self.request, 'Guest checked out successfully!')
        form.send_mail_to_guest()

        return HttpResponseRedirect(self.get_success_url())
