from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Login


# Create your views here.
class CreateBook(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [AllowAny]

class Authentication(generics.ListCreateAPIView):
    
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class Login(generics.ListCreateAPIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
        
class UpdateBook(generics.RetrieveUpdateAPIView):
     
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UpdateUser(generics.RetrieveUpdateAPIView):
     
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class DetailsBook(generics.RetrieveAPIView):
     
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DetailsUser(generics.RetrieveAPIView):
     
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class DeleteBook(generics.DestroyAPIView):
     
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DeleteUser(generics.DestroyAPIView):
     
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer


