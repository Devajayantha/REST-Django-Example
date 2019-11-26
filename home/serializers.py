from rest_framework import serializers
from .models import Inventory


class InventorySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id','url','name','paradigma')