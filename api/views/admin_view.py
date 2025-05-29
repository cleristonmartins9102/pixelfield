from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required

from ..models import BookModel

@staff_member_required
def adminView(request: HttpRequest) -> HttpResponse:
    books = BookModel.objects.all()
    return render(request, 'pages/admin/admin_page.html', { 'books': books })