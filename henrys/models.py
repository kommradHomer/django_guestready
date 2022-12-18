from django.db import models

# Create your models here.
from django.db import models
from django.utils.timezone import now

class Rental(models.Model):
    name = models.CharField(max_length=512)
    date_created =  models.DateTimeField(default=now, editable=False)
    date_updated =  models.DateTimeField(default=now)

class Reservation(models.Model):
    rental = models.ForeignKey(Rental,related_name="reservations",on_delete=models.DO_NOTHING,blank=False,null=False)
    checkin = models.DateField(null=False)
    checkout = models.DateField(null=False)
    date_created = models.DateTimeField(default=now, editable=False)
    date_updated =  models.DateTimeField(default=now)