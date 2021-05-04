from django.db import models
from datetime import date
from django.forms import ModelForm, modelformset_factory, ModelMultipleChoiceField, SelectMultiple, CheckboxSelectMultiple, TextInput, DateInput

# Create your models here.

class Attendance(models.Model):
    case = models.ForeignKey('Case', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.case) + " " +str(self.event)

class Event(models.Model):

    venue_name = models.CharField(max_length=200)
    venue_location = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    x_coordinate = models.DecimalField(max_digits=10, decimal_places=3)
    y_coordinate = models.DecimalField(max_digits=10, decimal_places=3)
    date = models.DateField(default=date.today)
    description = models.CharField(max_length=200)
    cases = models.ManyToManyField('Case', through=Attendance, blank=True)

    def __str__(self):
        return self.venue_name

class Case(models.Model):
    case_number = models.CharField(max_length=200)
    person_name = models.CharField(max_length=200)
    id_number = models.CharField(max_length=200)
    birth = models.DateField(default=date.today)
    onset_date = models.DateField(default=date.today)
    confirm_date = models.DateField(default=date.today)
    events = models.ManyToManyField('Event', through=Attendance, blank=True)

    def __str__(self):
        return self.case_number


