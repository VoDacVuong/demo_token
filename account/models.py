from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
import uuid
class MyUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    full_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique = True)

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user_uuid = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='Tag_UserProfile')
    avatar = models.ImageField(upload_to="my_image", blank=True)
    job = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user_uuid)

