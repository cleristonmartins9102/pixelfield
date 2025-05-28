from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from ..models import UserModel

def usersAdminView(request: HttpRequest) -> HttpResponse:
    users = UserModel.objects.all()
    return render(request, 'pages/admin/users/users_admin_page.html', { 'users': users })