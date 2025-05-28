from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from ..models import BookModel

def adminView(request: HttpRequest) -> HttpResponse:
    books = BookModel.objects.all()
    return render(request, 'pages/admin/admin_page.html', { 'books': books })