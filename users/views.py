from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate

from users.models import User
from users.serializers import UserCreateSerializer
from users.serializers import MyTokenObtainPairSerializer

class SignUpView(APIView):
    def post(self,request):
        user_serializer = UserCreateSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogInView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.get(email = email)
        
        if user is None:
            return Response({'msg':'없는 사용자입니다.'}, status = status.HTTP_404_NOT_FOUND)

        if not check_password(password, user.password):
            return Response({'msg':'비밀번호를 다시 입력해주세요'}, status=status.HTTP_400_BAD_REQUEST)
       
        user = authenticate(email=email, password=password)
        
        if user.is_authenticated:
            token = MyTokenObtainPairSerializer.get_token(user)
            refresh_token=str(token)
            access_token = str(token.access_token)
            return Response(
                {"access": access_token, "refresh": refresh_token},
                status=status.HTTP_200_OK)
        
        return Response(status = status.HTTP_400_BAD_REQUEST)
