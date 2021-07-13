import account
import supplier
from django.db import models
import uuid
# Create your models here.
# from account.models import *
class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    description = models.CharField(max_length=100)
    # user_profile = models.ForeignKey(, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name

class Product(models.Model):
    price = models.IntegerField()
    product_code = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique = True)

    description = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to="image_product", blank=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
