from django.urls import path
from register.views import EmployeeDetailsAPIView,EmployeeUpdateAPIView


urlpatterns = [
    # path('api/test/', TestAPIView.as_view()),
    path('api/emp/details/', EmployeeDetailsAPIView.as_view()),
    path('api/emp/update/<int:pk>', EmployeeUpdateAPIView.as_view())
]