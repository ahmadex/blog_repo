from blog_app.models import Blog
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class BlogSerializer(serializers.ModelSerializer):

    title = serializers.CharField(required=True, validators=[UniqueValidator(queryset=Blog.objects.all())])
    body = serializers.CharField(required=True)
    class Meta:
        model = Blog
        fields = ('title','body')
