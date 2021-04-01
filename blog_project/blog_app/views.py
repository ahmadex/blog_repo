from django.shortcuts import render
from blog_app.models import Blog
from blog_app.serializers import BlogSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.


class BlogView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes= [JWTAuthentication]

    def get(self, request, pk=None):
        
        if pk is None:
            blog = Blog.objects.all()
            serialize = BlogSerializer(blog, many=True)
        else:
            try:
                blog = Blog.objects.get(id=pk)
            except:
                return Response('Blog Does Not Exist')
            serialize = BlogSerializer(blog)
        return Response(serialize.data)
    
    def post(self, request):

        serialize = BlogSerializer(data=request.data)

        if serialize.is_valid():
            serialize.save(author = request.user)
            return Response('Blog Created')
        else:
            return Response(serialize.errors)
    
    def put(self, request, pk):
        try:
            blog = Blog.objects.get(id=pk)
        except:
            return Response('Blog Does Not Exist')
        
        serialize = BlogSerializer(blog, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response('Blog Updated Successfully')
        else:
            return Response(serialize.errors)
    
    def patch(self, request, pk):
        try:
            blog = Blog.objects.get(id=pk)
        except:
            return Response('Blog Does Not Exist')
        
        serialize = BlogSerializer(blog, data=request.data, partial=True)
        if serialize.is_valid():
            serialize.save()
            return Response('Blog Updated Successfully')
        else:
            return Response(serialize.errors)
    
    def delete(self, request, pk):
        try:
            blog = Blog.objects.get(id=pk)
        except:
            return Response('Blog Does Not Exist')

        blog.delete()
        return Response('Blog Deleted')