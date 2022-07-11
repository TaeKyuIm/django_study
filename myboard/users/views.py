from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import RegisterSerializer, LoginSerializer

class RegisterView(generics.CreateAPIView): # 회원가입의 경우 회원 생성 기능만 있으면 되어서 굳이 다른 요청을 해줄 필요 없다.
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data # validate()의 리턴값인 token 받아옴.
        return Response({"token" : token.key})