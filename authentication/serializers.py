from .models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from dj_rest_auth.registration.serializers import RegisterSerializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password','email', 'role')


class CustomRegisterSerializer(RegisterSerializer):
    # Add or modify fields as needed
    role = serializers.CharField()
        


        
    