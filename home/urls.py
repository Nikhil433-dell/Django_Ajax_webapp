from django.urls import path
from home.views import DeleteVehicle, EditVehicle, VehicleList, Details, Index
from home import views


urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('details/<int:id>', Details.as_view(), name="details"),
    path('edit/<int:pk>', EditVehicle.as_view(), name="edit"),
    path('delete/<int:pk>', DeleteVehicle.as_view(), name="delete"),
    path('vehicle_list', VehicleList.as_view(), name="vehicle_list"),
]
