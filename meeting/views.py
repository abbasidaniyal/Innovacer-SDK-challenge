from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from twilio.rest import Client

from meeting_management import settings
from meeting.models import Host, Guest
from meeting.forms import HostForm, GuestForm, GuestFormCheckout


def send_sms(message, to):
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        to=to,
        from_='+17206062779',
    )
    print(message)
    

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

        # send sms
        my_sms = {
            'message': f'You have a new guest! {self.object.name} is here to meet you! ',
            'to': '+'+str(self.object.host_name.phone_no.country_code)+str(self.object.host_name.phone_no.national_number),
        }
        
        send_sms(my_sms["message"], my_sms["to"])
        
        # send mail to Host
        subject = 'You have a new guest!!!!'
        html_message = render_to_string('meeting/email_to_host.html', {"action": "created", "obj": {"Name": self.object.name, "Email": self.object.email,
                                                                                                    "Phone No": self.object.phone_no, "Check In Time": self.object.check_in_time, "Address": self.object.address_visited}, "id": self.object.id})
        my_message = strip_tags(html_message)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = self.object.host_name.email
        send_mail(subject, my_message, email_from, [recipient_list])

        return HttpResponseRedirect(self.get_success_url())


class GuestUpdateView(UpdateView):
    '''
    GuestUpdateView is used to update the checkout time of the Guest. It also sends an email to the Guest about his details,Host Details etc 
    '''
    model = Guest
    form_class = GuestFormCheckout
    success_url = reverse_lazy("home-page")
    template_name = 'meeting/guest_checkout.html'

    def get(self, request, *args, **kwargs):
        '''
        Used to redirect to homepage if check out time is already filled.
        '''
        if self.model.objects.get(pk=kwargs["pk"]).check_out_time is not None:

            messages.warning(self.request, "Guest already checked out!")

            return redirect(reverse_lazy("home-page"))

        else:
            return super(GuestUpdateView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        # setting the checkout time to current time
        self.object.check_out_time = timezone.now()

        super(GuestUpdateView, self).form_valid(form)
        messages.success(self.request, 'Guest checked out successfully!')

        # send mail to guest
        subject = 'Thank you for your visit!!!!!!'
        my_host = Host.objects.get(pk=self.object.host_name.id)
        html_message = render_to_string('meeting/email_to_guest.html', {"action": "checkout", "obj": {"Name": my_host.name, "Email": my_host.email, "Phone No": my_host.phone_no,
                                                                                                      "Check In Time": self.object.check_in_time, "Check Out Time": self.object.check_out_time, "Address Visited": self.object.address_visited}, })

        message = strip_tags(html_message)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = self.object.email
        send_mail(subject, message, email_from, [recipient_list])

        return redirect(reverse_lazy("home-page"))
