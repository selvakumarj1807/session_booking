from django.db import models
from admin_panel.models import Session

class Session_booking(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Session_booking"

    def __str__(self):
        return f"{self.session.subject} booked by {self.username}"
