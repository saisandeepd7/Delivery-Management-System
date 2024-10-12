from rest_framework import generics, views
from .models import Component, Vehicle, Issue
from .serializers import ComponentSerializer, VehicleSerializer, IssueSerializer
from django.db.models import Sum
from django.http import JsonResponse
from datetime import datetime, timedelta

# API to handle CRUD for Components
class ComponentListCreateView(generics.ListCreateAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

# API to handle CRUD for Vehicles
class VehicleListCreateView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

# API to handle CRUD for Issues
class IssueListCreateView(generics.ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

# API to calculate the final price for all issues related to a vehicle
class FinalPriceView(views.APIView):
    def get(self, request, vehicle_id):
        issues = Issue.objects.filter(vehicle__id=vehicle_id)
        total_price = sum([issue.get_price() for issue in issues])
        return JsonResponse({"total_price": total_price})

# API to get revenue (daily, monthly, yearly)
class RevenueView(views.APIView):
    def get(self, request, period):
        if period == 'daily':
            date_filter = datetime.now() - timedelta(days=1)
        elif period == 'monthly':
            date_filter = datetime.now() - timedelta(days=30)
        elif period == 'yearly':
            date_filter = datetime.now() - timedelta(days=365)
        else:
            return JsonResponse({"error": "Invalid period"}, status=400)

        revenue = Issue.objects.filter(created_at__gte=date_filter).aggregate(
            total=Sum('component__new_price' if 'new' in period else 'component__repair_price'))
        return JsonResponse({"revenue": revenue['total']})
