from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication


from ..models import BookModel
from ..serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [AllowAny()]
        return [IsAuthenticated()]

