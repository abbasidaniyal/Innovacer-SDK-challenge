from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Host(models.Model):
    name = models.TextField("Name",max_length=50)
    email = models.EmailField("Email", max_length=254)
    phone_no = PhoneNumberField("Phone No")

    
class Guest(models.Model):
    name = models.TextField("Name",max_length=50)
    email = models.EmailField("Email", max_length=254)
    phone_no = PhoneNumberField("Phone No")
    check_in_time = models.TimeField(_("Check in time"), auto_now=True, )
    check_out_time = models.TimeField(_("Check out time"), auto_now=False)
    address_visited = models.TextField(_("Address/Room Visited"))
    host_name = models.ForeignKey(Host, verbose_name=_("Host Name"), on_delete=models.PROTECT)