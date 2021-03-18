from django.shortcuts import render
from rest_framework import generics
from user.models import User
from user.serializers import RegisterSerializer, LoginSerializer
from django.http import HttpResponse, HttpRequest, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
import hashlib
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth import authenticate


# Create your views here.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }

@permission_classes([AllowAny])
class LoginDetail(APIView):

    def get_object(self, data):
        try:
            return DjangoUser.objects.get(username = data['Username'], password = data['Password'])
        except DjangoUser.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        token_user =  authenticate(username= request.data['Username'], password= request.data['Password']) # django backend auth
        return Response(data= get_tokens_for_user(token_user), status=status.HTTP_200_OK)

@permission_classes([AllowAny])
class RegisterDetail(APIView):

    def get_object(self, username):
        try:
            existing_user = DjangoUser.objects.get(username = username)
        except DjangoUser.DoesNotExist:
            return False
        return True

    def save_django_user(self, data):
        user = DjangoUser.objects.create_user(username= data['Username'], email= data['EmailAddress'], password = data['Password'])
        user.save()


    def post(self, request, format=None):
        data = request.data
        existing_user = self.get_object(username= data['Username'])
        if (existing_user == True):
            return Response(data= {'error': 'User already exists'}, status= status.HTTP_403_FORBIDDEN)
        else:
            self.save_django_user(data = data) # for django auth
            return Response('User created', status=status.HTTP_201_CREATED)