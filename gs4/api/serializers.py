from rest_framework import serializers
from .models import Student

# Validators
def start_with_r(value):
    if value[0].lower != 'r':
        raise serializers.ValidationError("Name should start with R")


class StudentSerializer (serializers.Serializer):
    # name = serializers.CharField(max_length=100, validators=[start_with_r])
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    # This method is to post data means to create
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    # This method we use to update the existing data means
    def update(self, instance, validated_data):
        print(instance.name) # it will give us an old data
        instance.name = validated_data.get('name', instance.name)
        print(instance.name)  # it will give us an new udpated data
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    #Field level validations
    # This will be checked in our view method when it comes in is valid method
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("Seats are full")
        return value
    
    # Object level validations
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
            raise serializers.ValidationError("City must me Ranchi")
        return data

    