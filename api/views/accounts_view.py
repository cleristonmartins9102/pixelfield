from rest_framework import viewsets

from ..models import UserModel
from ..serializers import UserSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
        