from django.urls import path, include

from api.views import listOfBooksView
from api.views import loginView
from api.views import listOfBorrowBooksView, adminView, usersAdminView, booksAdminView

urlpatterns = [
    path('admin/', adminView),
    path('admin/books', booksAdminView),
    path('admin/users', usersAdminView),
    path('api/', include('api.urls')),
    path('books/', listOfBooksView, name='listOfBooksView'),
    path('borrow/', listOfBorrowBooksView, name='borrow'),
    path('login/', loginView, name='login'),

]
