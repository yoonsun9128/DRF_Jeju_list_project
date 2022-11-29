from rest_framework import serializers
from user.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

    def update(self, validated_updata):
        user = super().create(validated_updata) # todo 수정
        password = user.password
        user.set_password(password)
        user.save()
        return user
    
    def validate(self, data):
        if not len(data.get("username", "")) >= 4:
            raise serializers.ValidationError(
                detail={"error": "username의 길이는 4자리 이상이어야 합니다."}
            )
        if not len(data.get("password", "")) >= 4:
            raise serializers.ValidationError(
                detail={"error": "password의 길이는 4자리 이상이어야합니다."}
            )
        return data

        
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username

        return token