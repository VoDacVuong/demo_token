from django.db import models
from django.contrib.auth.models import AbstractUser
from supplier.models import Company 
# Create your models here.
import uuid
class MyUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique = True)

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user_uuid = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to="my_image", blank=True)
    job = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(self.user_uuid)

