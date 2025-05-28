from django.shortcuts import render
from django.test import TestCase, Client
from django.http import HttpRequest, HttpResponse

from ..models import BookModel
def listOfBooksView(request: HttpRequest) -> HttpResponse:
    books = BookModel.objects.all()
    return render(request, 'pages/books/list/list_books_page.html', { 'books': books })


class ListOfBooksViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.book1 = BookModel.objects.create(title="Book 1", author="Author 1")
        self.book2 = BookModel.objects.create(title="Book 2", author="Author 2")

    def test_list_books_view_status_code(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)

    def test_list_books_view_template_used(self):
        response = self.client.get('/books/')
        self.assertTemplateUsed(response, 'pages/books/list/list_books_page.html')

    def test_list_books_view_context(self):
        response = self.client.get('/books/')
        books = response.context['books']
        self.assertIn(self.book1, books)
        self.assertIn(self.book2, books)