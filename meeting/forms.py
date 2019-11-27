from django.forms import ModelForm
from meeting.models import Guest, Host




class GuestFormCheckout(ModelForm):
    def send_mail_to_guest(self,obj):
        subject = 'Thank you for your visit!'
        message = f''
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ''
        send_mail(subject,message,email_from,recipient_list)

    class Meta:
        model = Guest
        fields = []


class GuestForm(ModelForm):
    def send_mail_to_host(self):
        subject = ''
        message = ''
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ''
        send_mail(subject,message,email_from,recipient_list)

    def send_sms_to_host(self):
        pass

    class Meta:
        model = Guest
        fields = ["name", "email", 'phone_no', "address_visited", 'host_name']


class HostForm(ModelForm):

    class Meta:
        model = Host
        fields = ["name", "email", 'phone_no']
