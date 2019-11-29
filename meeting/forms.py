from django.forms import ModelForm
from meeting.models import Guest, Host
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    pass


class GuestFormCheckout(ModelForm): 
    class Meta:
        model = Guest
        fields = []


class GuestForm(ModelForm):
    

    
    class Meta:
        model = Guest
        fields = ["name", "email", 'phone_no', "address_visited", 'host_name']


class HostForm(ModelForm):

    class Meta:
        model = Host
        fields = ["name", "email", 'phone_no']
