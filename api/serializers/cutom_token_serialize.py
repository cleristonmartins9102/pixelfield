from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = getattr(user, 'role', None)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['role'] = getattr(self.user, 'role', None)
        return data