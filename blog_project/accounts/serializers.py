from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from accounts.models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):

    # password2 = serializers.CharField(style={'input-type':'password'}, write_only=True)
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','phone_no','password']

        # def save(self, validate_data):
        #     import pdb
        #     pdb.set_trace()
        #     print('validate', validate_data)
        #     user = User(username=self.validate_data['username'], email=self.validate_data['email'], phone_no=self.validate_data['phone_no'])

        #     password = self.validate_data['password']
        #     password2 = self.validate_data['password2']

        #     if password != password2:
        #         raise serializer.ValidationError({'password':'Password Didnt Match'})
                        
        #     user.set_password(password)
        #     user.save()
        #     return user
        
        def create(self, validated_data):
            
            user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_no = validated_data['phone_no']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user

