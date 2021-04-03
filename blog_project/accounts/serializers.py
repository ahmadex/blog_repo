from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from accounts.models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','phone_no','password','confirm_password']
        extra_kwargs = {
            'first_name':{'required':True},
            'last_name':{'required':True},
            'phone_no':{'required':True},
        }

    def create(self, validated_data):
        
        user = User(username=self.validated_data['username'], email=self.validated_data['email'], phone_no=self.validated_data['phone_no'], first_name=self.validated_data['first_name'], last_name=self.validated_data['last_name'])

        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']

        if password != password2:
            raise serializers.ValidationError({'password':'Password Didnt Match'})
                    
        user.set_password(password)
        user.save()
        return user
    

