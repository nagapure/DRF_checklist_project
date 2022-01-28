
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Once the URL hit- it will go to view and call the student_api method
    path('studentapi/', views.StudentAPI.as_view())
]
