from django.db import models
from django.utils import timezone

import datetime

class Session(models.Model):
    
    subject = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    # Add more fields like tutor name, location, etc., as needed
    
    class Meta:
        db_table = "Session"


    def __str__(self):
        return f"{self.subject} session on {self.date} at {self.time}"


class CustomUser(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "CustomUser"
    
    def __str__(self) :
        return self.name
