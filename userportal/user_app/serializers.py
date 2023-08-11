from .models import User
from rest_framework import serializers
from .constants import errors
import re

class UserSerializer(serializers.ModelSerializer):

    def validate(self,data):

        email = data.get('email')
        password = data.get('password')
        mobile = data.get('mobile')

        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
        password_regex = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        mobile_regex = r'^\d{10}$'

        if re.match(email_regex,email) is None:
            raise serializers.ValidationError(errors.get('INVALID_EMAIL_FORMAT'))
        
        if re.match(password_regex,password) is None:
            raise serializers.ValidationError(errors.get('INVALID_PASSWORD_FORMAT'))
        
        if re.match(mobile_regex,mobile) is None:
            raise serializers.ValidationError(errors.get('INVALID_MOBILE_FORMAT'))

        return data 
    
    class Meta:
        model = User
        fields = ['id','email','password','mobile','username']

class LoginSerializer(serializers.Serializer):

    email = serializers.CharField()
    password = serializers.CharField()


    def validate(self,data):

        email = data.get('email')
        password = data.get('password')

        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
        password_regex = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

        if re.match(email_regex,email) is None:
            raise serializers.ValidationError(errors.get('INVALID_EMAIL_FORMAT'))
        
        if re.match(password_regex,password) is None:
            raise serializers.ValidationError(errors.get('INVALID_PASSWORD_FORMAT'))
        
        return data 




