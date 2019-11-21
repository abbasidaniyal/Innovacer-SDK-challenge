from django.forms import ModelForm
from meeting.models import Guest, Host


class GuestForm(ModelForm):
    def send_mail_to_host(self):
        pass

    def send_sms_to_host(self):
        pass

    def send_mail_to_guest(self):
        pass

    class Meta:
        model = Guest
        fields = ["name", "email", 'phone_no', "address_visited", 'host_name']


class HostForm(ModelForm):

    class Meta:
        model = Host
        fields = ["name", "email", 'phone_no']
