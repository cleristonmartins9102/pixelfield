from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def listOfBorrowBooksView(request: HttpRequest) -> HttpResponse:
    return render(request, 'pages/books/list/list_borrow_books_page.html')