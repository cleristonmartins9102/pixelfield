from rest_framework import serializers
from ..models import LoanModel, BookModel
from ..serializers import  BookSerializer

class LoanSerializer(serializers.ModelSerializer): # type: ignore
    book_detail = BookSerializer(source='book', read_only=True)
    book = serializers.PrimaryKeyRelatedField(queryset=BookModel.objects.all())

    class Meta: # type: ignore
        model = LoanModel
        fields = ['book', 'book_detail', 'borrow', 'returned_date', 'is_returned', 'id']
