from django.urls import path, include

from .views import  LoginApiView, RegistrationApiView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('register/', RegistrationApiView.as_view(), name='register'),
    path('login/', LoginApiView.as_view(), name="login"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]