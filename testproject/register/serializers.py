from rest_framework import serializers
from register.models import EmployeeDetails

class EmployeeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetails
        fields = '__all__'