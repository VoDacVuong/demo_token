import re
from django.shortcuts import render
from django.utils.tree import Node
from . import serializer
from . import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from datetime import datetime
from django.utils import timezone
from account.models import UserProfile
from account.serializer import UserProfileSerializer

@api_view(['GET'])
def ListCompany(req):
    lst_company = models.Company.objects.all()
    serial = serializer.CompanySerializer(lst_company, many=True)
    return Response({'errorCode': 0,'messages': 'successfully', 'current_t': datetime.timestamp(timezone.now()),"data": serial.data})

@api_view(['GET'])
def DetailCompany(req, key):
    company = models.Company.objects.get(id=key)
    serial = serializer.CompanySerializer(company)
    lst_product = models.Product.objects.filter(company_id=key)

    lst_userprofile = UserProfile.objects.filter(company_id=key)
    # import pdb; pdb.set_trace()
    lst_userprofile = [UserProfileSerializer(x).data for x in lst_userprofile]

    lst_product = [serializer.ProductSerializer(x).data for x in lst_product]

    data = [{
        'company': serial.data,
        'product':lst_product,
        'user_profile': lst_userprofile
    }]


    return Response({'errorCode': 0,'messages': 'successfully', 'current_t': datetime.timestamp(timezone.now()),"data": data})
      
@api_view(['POST'])
def CreateCompany(req):
    post_data = req.POST
    company = models.Company()
    company.name = post_data.get('name')
    company.address = post_data.get('address')
    company.phone = post_data.get('phone')
    company.description = post_data.get('description')
    company.save()
    serial = serializer.CompanySerializer(company)
    return Response({'errorCode': 0,'messages': 'successfully', 'current_t': datetime.timestamp(timezone.now()),"data": serial.data})

@api_view(['POST'])
def UpdateCompany(req, key):
    post_data = req.POST
    company = models.Company.objects.get(id=key)
    company.name = post_data.get('name')
    company.address = post_data.get('address')
    company.phone = post_data.get('phone')
    company.description = post_data.get('description')
    company.save()
    serial = serializer.CompanySerializer(company)
    return Response({'errorCode': 0,'messages': 'successfully', 'current_t': datetime.timestamp(timezone.now()),"data": serial.data})

# --------------

@api_view(['GET'])
def ListProduct(req):
    product = models.Product.objects.all()
    seria = serializer.ProductSerializer(product, many=True)
    return Response({'errorCode': 0,'messages': 'successfully', 'current_t': datetime.timestamp(timezone.now()),"data": seria.data})
    
@api_view(['GET'])
def DetailProduct(req, uuid):
    product = models.Product.objects.get(product_code=uuid)
    serial = serializer.ProductSerializer(product)
    return Response({'errorCode': 0,'messages': 'successfully', 'current_t': datetime.timestamp(timezone.now()),"data": serial.data})

@api_view(['POST'])
def CreateProduct(req):
    post_data = req.POST
    product = models.Product()
    product.price = post_data.get('price')
    product.description = post_data.get('description')
    product.image = req.FILES.get('image')
    # product.create_at = post_data.get('create_at')
    # product.update_at = post_data.get('update_at')
    product.company_id = int(post_data.get('company'))

    # import pdb; pdb.set_trace()
    product.save()
    serial = serializer.ProductSerializer(product)
    return Response({'errorCode': 0,'messages': 'successfully', 'current_t': datetime.timestamp(timezone.now()),"data": serial.data})

@api_view(['POST'])
def UpdateProduct(req, uuid):
    post_data = req.POST

    product = models.Product.objects.get(product_code=uuid)
    product.price = post_data.get('price')
    if post_data.get('description') != None:
        # product.description = product.description
    
        product.description = post_data.get('description')
    product.image = req.FILES.get('image')
    product.company_id = int(post_data.get('company'))
    product.save()
    serial = serializer.ProductSerializer(product)
    return Response({'errorCode': 0,'messages': 'successfully', 'current_t': datetime.timestamp(timezone.now()),"data": serial.data})
