from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','email', 'password','birthdate']
    extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)