from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.serializers import UserCreateSerializer


class SignUpView(APIView):
    def post(self,request):
        user_serializer = UserCreateSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)