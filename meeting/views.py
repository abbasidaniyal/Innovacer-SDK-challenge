from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect


from meeting.models import Host, Guest
from meeting.forms import HostForm, GuestForm


def HomePage(request):
    return render(request,"meeting/index.html",)

class HostCreateView(CreateView):

    model = Host
    form_class = HostForm
    success_url = ''
    template_name = "meeting/host.html"
    def get_success_url(self):
        return reverse('home-page')


    def form_valid(self, form):
        super(HostCreateView, self).form_valid(form)

        messages.success(self.request, 'Host Added successfully!')
        return HttpResponseRedirect(self.get_success_url())


class GuestCreateView(CreateView):
    model = Guest
    template_name = "meeting/guest.html"
    
    form_class = GuestForm

    def get_success_url(self):
        return reverse('home-page')

    def form_valid(self, form):
        super(GuestCreateView, self).form_valid(form)

        messages.success(self.request, 'Guest Added successfully!')
        form.send_sms_to_host()
        form.send_mail_to_host()
        return HttpResponseRedirect(self.get_success_url())


class GuestUpdateView(UpdateView):
    model = Guest
    template_name = "meeting/guest.html"


     def form_valid(self, form):
        super(GuestCreateView, self).form_valid(form)

        messages.success(self.request, 'Guest checked out successfully!')
        form.send_mail_to_guest()
        return HttpResponseRedirect(self.get_success_url())

