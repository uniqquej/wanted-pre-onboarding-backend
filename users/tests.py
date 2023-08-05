from rest_framework.test import APITestCase
from django.test import TestCase
from django.urls import reverse
from users.models import User
from users.serializers import UserCreateSerializer
from rest_framework.serializers import ValidationError

class SignUpTest(APITestCase):
    def test_sign_up(self):
        url = reverse('sign_up')
        user_data = {
            "email":"test@test.com",
            "password":"testpass",
            "password2":"testpass"
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code,201)
            
class UserCreateSerializerErrorTest(TestCase):
    def test_password_not_match_error(self):
        user_data = {
            "email":"test@test.com",
            "password":"testpassword",
            "password2":"test"
        }
        
        serializer = UserCreateSerializer(data=user_data)
        with self.assertRaisesMessage(ValidationError, '비밀번호가 일치하지 않습니다.'):
            serializer.is_valid(raise_exception=True)
    
    def test_password_length_error(self):
        user_data = {
            "email":"test@test.com",
            "password":"test",
            "password2":"test"
        }
        
        serializer = UserCreateSerializer(data=user_data)
        with self.assertRaisesMessage(ValidationError, '비밀번호는 8자이상으로 설정해주세요.'):
            serializer.is_valid(raise_exception=True)
    
    def test_email_error(self):
        user_data = {
            "email":"testtest",
            "password":"testpass",
            "password2":"testpass"
        }
        
        serializer = UserCreateSerializer(data=user_data)
        with self.assertRaisesMessage(ValidationError, '@를 사용해서 이메일을 입력해주세요'):
            serializer.is_valid(raise_exception=True)