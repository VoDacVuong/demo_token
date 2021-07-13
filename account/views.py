from copy import error
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from . import serializer
from . import models
from django.utils import timezone
# Create your views here.
from datetime import datetime
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions


class LoginView(TokenObtainPairView):
    serializer_class = serializer.MyTokenObtainPairSerializer



@api_view(['GET'])
def ListUser(req):
    users = models.MyUser.objects.all()
    # import pdb;pdb.set_trace()
    # serial = serializer.MyUserSerializer(users)
    lst_user = [serializer.MyUserSerializer(x).data for x in users]
    return Response({'errorCode': 0,'messages': 'successfully', 'current_t': datetime.timestamp(timezone.now()),"data": lst_user})

@api_view(['GET'])
def UserDetail(req, uuid):
    
    user = models.MyUser.objects.get(uuid=uuid)
    serial = serializer.MyUserSerializer(user)

    user_profile = models.UserProfile.objects.filter(user_uuid_id=uuid)
    # import pdb;pdb.set_trace()
    serial1 = serializer.UserProfileSerializer(user_profile, many=True)
    data = {
        'user': serial.data,
        'user_profile': serial1.data
    }


    return Response({'errorCode': 0,'messages': 'successfully', 'current_t': datetime.timestamp(timezone.now()),"data": data})

@api_view(['POST'])
def CreateUser(req):
    permission_classes = (permissions.AllowAny,)
    post_data = req.POST
    user = models.MyUser()
    user.username = post_data.get('username')
    user.email = post_data.get('email')
    user.set_password(post_data.get('password'))
    # import pdb;pdb.set_trace()
    # user.save()
    serial = serializer.MyUserSerializer(user)
    return Response({'errorCode': 0,'messages': 'successfully', 'current_t': datetime.timestamp(timezone.now()),"data": serial.data})

@api_view(['POST'])
def UpdateUser(req, uuid):
    post_data = req.POST
    user = models.MyUser.objects.get(uuid=uuid)
    user.username = post_data.get('username')
    user.email = post_data.get('email')
    user.set_password(post_data.get('password'))
    user.save()
    serial = serializer.MyUserSerializer(user)
    return Response({'errorCode': 0,'messages': 'successfully', 'current_t': datetime.timestamp(timezone.now()),"data": serial.data})

# ---------------

@api_view(['GET'])
def ListProfile(req):
    lst_profile = models.UserProfile.objects.all()
    serial = serializer.UserProfileSerializer(lst_profile, many=True)
    return Response({'errorCode': 0,'messages': 'successfully', 'current_t': datetime.timestamp(timezone.now()),"data": serial.data})

@api_view(['GET'])
def DetailProfile(req, key):
    profile = models.UserProfile.objects.get(id=key)
    serial = serializer.UserProfileSerializer(profile)
    return Response({'errorCode': 0,'messages': 'successfully', 'current_t': datetime.timestamp(timezone.now()),"data": serial.data})

@api_view(['POST'])
def CreateProfile(req):
    post_data = req.POST
    profile = models.UserProfile()
    profile.user_uuid = models.MyUser.objects.get(uuid=post_data.get('user_uuid'))
    # import pdb;pdb.set_trace()
    profile.avatar = req.FILES['avatar']
    profile.job = post_data.get('job')
    profile.company_id = int(post_data.get('company'))
    profile.full_name = post_data.get('full_name')

    profile.save()
    serial = serializer.UserProfileSerializer(profile)
    return Response({'errorCode': 0,'messages': 'successfully', 'current_t': datetime.timestamp(timezone.now()),"data": serial.data})

@api_view(['POST'])
def UpdateProfile(req, key):
    post_data = req.POST
    profile = models.UserProfile.objects.get(id=key)
    profile.user_uuid = models.MyUser.objects.get(uuid=post_data.get('user_uuid'))
    profile.avatar = req.FILES['avatar']
    profile.job = post_data.get('job')
    profile.company = post_data.get('company')

    profile.save()
    serial = serializer.UserProfileSerializer(profile)
    return Response({'errorCode': 0,'messages': 'successfully', 'current_t': datetime.timestamp(timezone.now()),"data": serial.data})





    
        







