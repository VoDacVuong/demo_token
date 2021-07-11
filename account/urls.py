from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path("user/", views.ListUser),
    path('user/<uuid:uuid>/', views.UserDetail),
    path('user/create/', views.CreteUser),
    path('user/update/<uuid:uuid>/', views.UpdateUser),
    path('profile/', views.ListProfile),
    path('profile/<int:key>/', views.DetailProfile),
    path('profile/create/', views.CreateProfile),
    path('profile/update/<int:key>/', views.UpdateProfile),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', views.LoginView.as_view()),

]
    