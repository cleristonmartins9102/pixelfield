from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def loginView(request: HttpRequest) -> HttpResponse:
    return render(request, 'pages/login/login_page.html')