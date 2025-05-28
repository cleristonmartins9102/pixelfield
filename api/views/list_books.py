from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from ..models import BookModel
def listOfBooksView(request: HttpRequest) -> HttpResponse:
    books = BookModel.objects.all()
    return render(request, 'pages/books/list/list_books_page.html', { 'books': books })