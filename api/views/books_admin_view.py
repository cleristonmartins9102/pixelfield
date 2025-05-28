from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from ..models import BookModel

def booksAdminView(request: HttpRequest) -> HttpResponse:
    books = BookModel.objects.all()
    return render(request, 'pages/admin/books/books_admin_page.html', { 'books': books })