from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status, generics, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from user.serializers import UserSerializer

class SignupView(generics.CreateAPIView):

    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

signup = SignupView.as_view()
