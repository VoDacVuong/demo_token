from django.db.models import fields
from rest_framework import serializers
from . import models

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = models.Product
        fields = '__all__'