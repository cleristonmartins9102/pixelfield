from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponse

def logoutView(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('login/')