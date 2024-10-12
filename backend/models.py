from django.db import models
from django.utils import timezone

class Component(models.Model):
    name = models.CharField(max_length=255)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    repair_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

class Issue(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    is_repair = models.BooleanField(default=True)  # True for repair, False for new component
    created_at = models.DateTimeField(default=timezone.now)

    def get_price(self):
        return self.component.repair_price if self.is_repair else self.component.new_price

    def __str__(self):
        return f"Issue with {self.vehicle} on {self.component}"
