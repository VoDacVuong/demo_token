from django.urls import path
from . import views
urlpatterns = [
    path('company/', views.ListCompany),
    path('company/<int:key>/', views.DetailCompany),
    path('company/create/', views.CreateCompany),
    path('company/update/<int:key>/', views.UpdateCompany),
    path('product/', views.ListProduct),
    path('product/<uuid:uuid>/', views.DetailProduct),
    path('product/create/', views.CreateProduct),
    path('product/update/<uuid:uuid>/', views.UpdateProduct),



]

