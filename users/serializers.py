from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User

class UserCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['email','password','password2']
        
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('비밀번호가 일치하지 않습니다.')
        
        elif len(data['password'])<8:
            raise serializers.ValidationError('비밀번호는 8자이상으로 설정해주세요.')
        
        if '@' not in data['email']:
            raise serializers.ValidationError('@를 사용해서 이메일을 입력해주세요')

        data.pop('password2')
        
        return data
    
    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
        

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    '''
    simple JWT에서 제공해주는 token serializer
    '''
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email
        
        return token