from rest_framework import serializers
from user.models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ['Username', 'EmailAddress', 'Password']

class LoginSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ['EmailAddress', 'Password']
