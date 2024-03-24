from django.db import models

# Create your models here.

# takes the customer details for the bookng

# class Customer_booking(models.Model):

# Holds the details of tables and sizes

# class Tables(models.Model):

# Holds a list of all the upcoming events

class Events(models.Model):
    event = models.CharField(max_length=200)
    details = models.TextField(blank=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=False, **options)
    time = models.DateTimeField(auto_now=False, auto_now_add=False, **options)
    cost = models.DecimalField(max_digits=8 blank=True)

    class Meta:
        ordering = ['date']
        indexes = [
            models.Index(fields=['date']),
        ]
        verbose_name= 'events'
        verbose_name_plural = 'events'

    def __str__(self):
        return str(self.name)
