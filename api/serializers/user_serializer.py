from rest_framework import serializers

from ..models import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta: # type: ignore
        model = UserModel
        fields = [
            'id',
            'username', 
            'email',
            'role',
            'first_name',
            'last_name',
            'password',
            'is_active',
            'date_joined'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

        def create(self, validated_data): # type: ignore
            user = UserModel.objects.create_user(**validated_data) # type: ignore
            user.save()
            return user
