from django.db import models
from datetime import datetime
# Create your models here.
class ReportAnonymously(models.Model):
    Incident_Date=models.DateField(null=True,blank=True)
    Location_of_Crime=models.CharField(max_length=100, default="")
    Crime= models.TextField(default="")
    date_subscribed = models.DateTimeField(default=datetime.now())

class Report(models.Model):
    
    name = models.CharField(max_length=50, default="")
    Email_ID=models.EmailField(max_length=100, default="")
    contact_No = models.CharField(max_length=50, default="")
    Adress=models.CharField(max_length=100, default="")
    date_subscribed = models.DateTimeField(default=datetime.now())
    Location_of_Crime=models.CharField(max_length=100, default="")
    Crime= models.TextField(max_length=500,default="")

    
    