from __future__ import unicode_literals

from django.db import models

class Request(models.Model):
    raisedBy = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    reqStatus = models.BooleanField()

    def __str__(self):
        return "Request %s : raised by  %s : status %s" % (self.timestamp, self.raisedBy, self.reqStatus)

class User(models.Model):
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=10)
    security_hash = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=100, primary_key=True) ## setting a field as primary key
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

class Manufacturer(models.Model):
    name = models.CharField(max_length=30)

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

## many to many relationship
## For example, if a Pizza has multiple Topping Objects - that is, a Topping can
## be on multiple pizzas and each Pizza has multiple topings here's how you'd represent that:
class Topping(models.Model):
    # ...
    pass

class Pizza(models.Model):
    # ...
    toppings = models.ManyToManyField(Topping)