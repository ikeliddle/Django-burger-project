import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Login(models.Model):
    username_text = models.CharField(max_length=30)
    password_text = models.CharField(max_length=30)
    date_reg = models.DateTimeField('date registered', auto_now=True)
    def __str__(self):
        return self.username_text + " " + self.password_text
    def was_registered_recently(self):
        return self.date_reg >= timezone.now() - datetime.timedelta(days=1)

class Interest(models.Model):
    name = models.CharField(max_length=20)
    date_applied = models.DateTimeField('Date Applied', auto_now=True)
    def __str__(self):
        return self.name
    def was_applied_intime(self):
        return self.date_applied >= timezone.now() - datetime.timedelta(days=1)

class Maxinterest(models.Model):
    maximum = models.CharField(max_length=3)
    cutoff_date = models.DateTimeField('cutoff date')
    def __str__(self):
        return self.maximum
    def cutoff_yes(self):
        return self.cutoff_date >= timezone.now() - datetime.timedelta(days=1)

class Mealdate(models.Model):
    next_meal = models.DateTimeField('next meal date')
