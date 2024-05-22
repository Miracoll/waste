from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.

class Waste(models.Model):
    name = models.CharField(max_length = 50, null=True, blank=True)
    location = models.CharField(max_length = 50, null=True, blank=True)
    occupied_percent = models.IntegerField(blank=True, null=True)
    battery_percent = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    ref = models.UUIDField(default=uuid4, editable=False)
    created_on = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name