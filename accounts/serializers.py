from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import CustomUser
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))

       
        if not any(char.isupper() for char in value):
            raise serializers.ValidationError('Password must contain at least one uppercase letter.')
        if not any(char.islower() for char in value):
            raise serializers.ValidationError('Password must contain at least one lowercase letter.')
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError('Password must contain at least one digit.')
        if not any(not char.isalnum() for char in value):
            raise serializers.ValidationError('Password must contain at least one special character.')

        return value

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            full_name=validated_data.get('full_name', ''),
            company_name=validated_data.get('company_name', ''),
            role_id=validated_data.get('role_id', None)
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
