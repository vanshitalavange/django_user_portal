from .models import User
from rest_framework import serializers
import re

class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    password = serializers.CharField()
    mobile = serializers.CharField()
    
    def validate_email(self,value):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'

        if re.match(pattern, value) is None:
            raise serializers.ValidationError("invalid email format")
        return value

    
    def validate_password(self,value):
        pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

        if re.match(pattern,value) is None:
            raise serializers.ValidationError("Password must contain one uppercas, one lowercase, one special character, one digit and length should be 8")
        return value 
    
    def validate_mobile(self,value):
        pattern = r'^\d{10}$'
        if re.match(pattern,value) is None:
            raise serializers.ValidationError("mobile number is invalid")
        return value

    class Meta:
        model = User
        fields = ['email','password','mobile','username']