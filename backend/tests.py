from django.test import TestCase
from .models import Component, Vehicle, Issue

class ComponentModelTest(TestCase):
    def setUp(self):
        Component.objects.create(name='Engine', new_price=5000, repair_price=1500)

    def test_component_creation(self):
        engine = Component.objects.get(name='Engine')
        self.assertEqual(engine.new_price, 5000)

class VehicleModelTest(TestCase):
    def setUp(self):
        Vehicle.objects.create(make='Toyota', model='Corolla', year=2015)

    def test_vehicle_creation(self):
        vehicle = Vehicle.objects.get(make='Toyota')
        self.assertEqual(vehicle.model, 'Corolla')
