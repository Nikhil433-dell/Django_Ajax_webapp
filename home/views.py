from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from home.models import Vehicle
from home.serializers import VehicleSerializer

# Create your views here.



class Index(CreateView):
    model = Vehicle
    fields = "__all__"
    template_name = "index.html"



class VehicleList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "vehicle_list.html"

    def get(self, request):
        vehicle_list = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicle_list, many=True)
        return Response({'serializer': serializer.data})



class Details(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "details.html"

    def get(self, request, id):
        vehicle = get_object_or_404(Vehicle, id=id)
        serializer = VehicleSerializer(vehicle)

        return Response({'serializer': serializer.data})



class EditVehicle(UpdateView):
    model = Vehicle
    template_name = "edit.html"
    fields = "__all__"


class DeleteVehicle(DeleteView):
    model = Vehicle
    template_name = "delete.html"
    success_url = reverse_lazy("vehicle_list")