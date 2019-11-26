from django.shortcuts import render
from rest_framework import viewsets
from .models import Inventory
from .serializers import InventorySerializers


class InventoryView(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializers
