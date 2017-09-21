from django.contrib.auth.models import User
from rest_framework import serializers

from ..models import Patient, Employee



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email',)


class PatientUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Patient
        fields = ('user',)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        patient = Patient.objects.create(user=user, **validated_data)
        return patient


class EmployeeUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = ('user', 'contact_phone')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data, is_staff=True)
        employee = Employee.objects.create(user=user, **validated_data)
        return employee
