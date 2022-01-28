from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



from login.views import TestAPIView,RegisterAPIView,LogOutAPIView
urlpatterns = [
    path('api/test/', TestAPIView.as_view()),
    path('api/login/', TokenObtainPairView.as_view(), name='login_view'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),
    path('api/logout/', LogOutAPIView.as_view(), name='logout_view'),

    path('api/register/',RegisterAPIView.as_view()),
]
