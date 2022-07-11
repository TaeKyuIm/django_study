from django.contrib.auth.models import User # User 모델
from django.contrib.auth.password_validation import validate_password # 패스워드 검증도구
from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.authtoken.models import Token # Token 도구
from rest_framework.validators import UniqueValidator # 이메일 중복 방지를 위한 검증 도구

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())] # 이메일에 대한 중복 검증
    )

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(write_only=True, required=True) # 비밀번호 확인용

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    def validate(self, data):
        if data['password'] != data['password2']: # 비밀번호 일치여부 확인
            raise serializers.ValidationError(
                {'password' : "Password fields didn't match."})
        return data

    def create(self, validated_data):
        # create 요청에 대해 create 메서드를 오버라이딩, 유저를 생성하고, 토큰 생성까지 함.
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True) # write_only = True 옵션을 통해 서버 -> 클라이언트 방향의 직렬화 불가

    def validate(self, data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user=user)
            return token
        raise serializers.ValidationError(
            {"error" : "Unable to log in with provided credentials."}
        )