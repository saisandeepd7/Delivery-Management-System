from django.urls import path
from .views import ComponentListCreateView, VehicleListCreateView, IssueListCreateView, FinalPriceView, RevenueView

urlpatterns = [
    path('components/', ComponentListCreateView.as_view(), name='component-list-create'),
    path('vehicles/', VehicleListCreateView.as_view(), name='vehicle-list-create'),
    path('issues/', IssueListCreateView.as_view(), name='issue-list-create'),
    path('final_price/<int:vehicle_id>/', FinalPriceView.as_view(), name='final-price'),
    path('revenue/<str:period>/', RevenueView.as_view(), name='revenue'),
]
