from django.contrib import admin
from django.urls import path, include

from api.views import listOfBooksView
from api.views import loginView
from api.views import listOfBorrowBooksView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('books/', listOfBooksView, name='listOfBooksView'),
    path('borrow/', listOfBorrowBooksView, name='borrow'),
    path('login/', loginView, name='login'),

]
