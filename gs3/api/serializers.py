from rest_framework import serializers
from .models import Student

class StudentSerializer (serializers.Serializer):
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
