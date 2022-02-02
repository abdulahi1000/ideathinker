from rest_framework import serializers

from django.contrib.auth.models import User
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']

class UserSerializerWithToken(UserSerializer):
    access_token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'access_token']
    
    def get_access_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model= UserProfile
        fields='__all__'
    
    def get_user(self, obj):
        user = obj.user
        serializer = UserSerializer(user, many=False)
        return serializer.data




