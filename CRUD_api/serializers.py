from rest_framework import serializers
from .models import Items
from django.db.models import fields

class ItemSerializer(serializers.ModelSerializer):
    category = serializers.CharField(required=True)
    subcategory = serializers.CharField(required=True)
    class Meta:
        model = Items
        fields = ('category', 'subcategory', 'name', 'amount')




