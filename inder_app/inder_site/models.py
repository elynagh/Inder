from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Idea(models.Model):
    idea_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    idea_title = models.CharField(max_length=280)
    text = models.CharField(max_length=1280)
    date_posted = models.DateTimeField(auto_now_add=True)
    hidden = models.BooleanField(default=False)
    date_hidden = models.DateTimeField(blank=True, null=True)
    hidden_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, blank=True, null=True, related_name='mod_who_hid') 

    def __str__(self):
        return self.text

class Report(models.Model):
    report_id = models.IntegerField(primary_key=True)
    reported_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    idea_id = models.ForeignKey(Idea, on_delete=models.CASCADE)

    def __str__(self):
        return self.text