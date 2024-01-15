from datetime import datetime
import uuid
from django.db import models


class Event(models.Model):
    name = models.CharField('Event Name', max_length=50)
    event_date = models.DateTimeField('Event Date')
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    venue = models.IntegerField(max_length=3)
    token_id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    mobile_no = models.CharField(max_length=12) 
    email_address = models.EmailField('Email Address')

    def __str__(self) -> str:
        return self.name