from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from django.contrib.auth import authenticate
from django.utils import timezone
        
# class RegisterSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#         required = True,
#         validators = [UniqueValidator(queryset=User.objects.all())]
#     )

#     class Meta:
#         model = User
#         fields = ['username', 'email',]

#     def create(self, validated_data):
#         user = User.objects.create(
#             username = validated_data['username'],
#             email = validated_data['email'],
#         )
#         user.save()
#         return user

# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     username = serializers.CharField(max_length=255, read_only=True)
#     last_login = serializers.CharField(max_length=255, read_only=True)

#     def validate(self, data):
#         email = data.get('email', None)
#         username = data.get('username', None)
        
#         user = authenticate(email=email, username=username)
        
#         if user is None:
#             raise serializers.ValidationError(
#                 'A user with this email was not found'
#             )
        
#         if not user.is_active:
#             raise serializers.ValidationError(
#                 'This user has been deactivated.'
#             )
        
#         user.last_login = timezone.now()
#         user.save(update_fields=['last_login'])
        
#         # 7.
#         return {
#             'email': user.email,
#             'username': user.username,
#             'last_login': user.last_login
#         }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'mbti']

