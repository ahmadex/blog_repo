from django.shortcuts import render
from accounts.serializers import UserSerializer
from accounts.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


class UserCreateView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        user = User.objects.all()
        serialize = UserSerializer(user, many=True)
        return Response(serialize.data)

    def post(self, request):
        serialize = UserSerializer(data=request.data)
        print('hello',request.data)
        data = {}
        if serialize.is_valid():
            user = serialize.save()
            user.set_password(serialize['password'])
            user.save()
            data['response'] = 'User Created Successfully'
            data['email'] = user.email
            data['username'] = user.username
            data['phone_no'] = str(user.phone_no)
        else:
            data = serialize.errors
        return Response(data)



