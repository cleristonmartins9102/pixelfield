from rest_framework import serializers
from ..models import BookModel

class BookSerializer(serializers.ModelSerializer): # type: ignore
    class Meta: # type: ignore
        model = BookModel
        fields = '__all__'