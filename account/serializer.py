from django.db.models import fields
from rest_framework import serializers
from . import models
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from datetime import datetime
from django.utils import timezone
from supplier.serializer import CompanySerializer
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self,user):
        print(user)
        data = super().validate(user)
        # print(data)
        # token = self.get_token(self.user)
        # data['user'] = str(self.user) 
        # data['uuid'] = str(self.user.uuid)
        # data['email'] = str(self.user.email)
        # print(data)
        # user_profile = models.UserProfile.objects.get(user_uuid_id=data['uuid'])
        # data['profile'] = user_profile.company
        data['error_code'] = "0"
        data['message'] = "successfully"
        data['current_t'] = datetime.timestamp(timezone.now())
        return data

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MyUser
        fields = ['uuid', 'first_name', 'last_name', 'username', 'email', 'is_active', 'is_staff', 'is_superuser']

class UserProfileSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    user_uuid = MyUserSerializer()
    class Meta:
        model = models.UserProfile
        fields = '__all__'