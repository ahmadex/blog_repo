from django.shortcuts import render
from accounts.serializers import UserSerializer
from accounts.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.


class UserCreateView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk=None):
        if pk is None:
            user = User.objects.all()
            serialize = UserSerializer(user, many=True)
        else:
            try:
                user = User.objects.get(id=pk)
            except:
                return Response(f'User does not exist at id:{pk}')
            serialize = UserSerializer(user)
        return Response(serialize.data)

    def post(self, request):
        serialize = UserSerializer(data=request.data)
        data = {}
        if serialize.is_valid():
            user = serialize.save()
            data['email'] = user.email
            data['username'] = user.username
            data['phone_no'] = str(user.phone_no)
        else:
            data = serialize.errors
        return Response(data)

    def put(self, request, pk):
        try:
            user = User.objects.get(id=pk)
        except:
            return Response(f'User doest not exists at id:{pk}')
        serialize = UserSerializer(user,data=request.data)
        data = {}
        if serialize.is_valid():
            user = serialize.save()
            data['sucess'] = 'User Updated Successfully'
        else:
            data = serialize.errors
        return Response(data)
    
    def patch(self, request, pk):
        try:
            user = User.objects.get(id=pk)
        except:
            return Response(f'User doest not exists at id:{pk}')
        serialize = UserSerializer(user,data=request.data, partial=True)
        data = {}
        if serialize.is_valid():
            user = serialize.save()
            data['Success'] = 'User Updated Sucessfully'
        else:
            data = serialize.errors
        return Response(data)

    def delete(self, request, pk):
        try:
            user = User.objects.get(id=pk)
        except:
            return Response(f'user with id: {pk} doesnot exist')
        user.delete()
        return Response({'msg':'User Deleted'})


        

def login(request):
    return render(request, 'accounts/login.html',)

