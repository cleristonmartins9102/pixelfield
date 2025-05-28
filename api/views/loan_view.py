from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from ..models import LoanModel, BookModel
from ..serializers import LoanSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = LoanModel.objects.all()
    serializer_class = LoanSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'], url_path='delete_loan')
    def delete_book(self, request: Request) -> Response:
        book_id = request.data.get('book_id')
        if not book_id:
            return Response({'detail': 'book_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            bookModel = LoanModel.objects.get(book_id=book_id)
            bookModel.delete()
            book = BookModel.objects.get(id=book_id)
            book.availability = True
            book.save()
            return Response({'detail': 'Book deleted'}, status=status.HTTP_204_NO_CONTENT)
        except BookModel.DoesNotExist:
            return Response({'detail': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def get_queryset(self):
        qs = LoanModel.objects.filter(user=self.request.user).select_related('book')
        return qs

    def perform_create(self, serializer): # type: ignore
        loan = serializer.save(user=self.request.user)
        book = loan.book # type: ignore
        book.availability = False # type: ignore
        book.save() # type: ignore


