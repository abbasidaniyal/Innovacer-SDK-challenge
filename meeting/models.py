from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Host(models.Model):

    def __str__(self):
        return self.name
    

    name = models.CharField("Name",max_length=50)
    email = models.EmailField("Email", max_length=254)
    phone_no = PhoneNumberField("Phone No")

    
    
class Guest(models.Model):

    def __str__(self):
        return self.name
    
    name = models.CharField("Name",max_length=50)
    email = models.EmailField("Email", max_length=254)
    phone_no = PhoneNumberField("Phone No")
    check_in_time = models.TimeField(("Check in time"), auto_now_add=True, )
    check_out_time = models.TimeField(("Check out time"), auto_now=False,null=True)
    address_visited = models.TextField(("Address/Room Visited"))
    host_name = models.ForeignKey(Host, verbose_name=("Host Name"), on_delete=models.PROTECT)

