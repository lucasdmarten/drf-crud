from django.contrib.auth import get_user_model
from core.models import Naver, Projeto
from rest_framework import  serializers


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username','email','password']
    extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_superuser(username=validated_data['username'],
                                    email = validated_data['email'],
                                    password = validated_data['password'])
        return user

class ProjetoSerializer(serializers.ModelSerializer):
    # users = UserSerializer(many=True)
    class Meta:
        model = Projeto
        fields = ['id', 'name', 'get_users_id']

class NaverSerializer(serializers.ModelSerializer):
    projetos = ProjetoSerializer(many=True, read_only=True  )
    class Meta:
        model = Naver
        fields = ['id','fullname','birthdate', 'admission_date', 'job_role', 'projetos']






