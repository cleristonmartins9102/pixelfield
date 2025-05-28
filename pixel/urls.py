from django.urls import path, re_path, include
from rest_framework import permissions
from api.views import listOfBooksView
from api.views import loginView
from api.views import listOfBorrowBooksView, adminView, usersAdminView, booksAdminView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Library API",
      default_version='v1',
      description="API documentation for the Library app",
      terms_of_service="https://www.example.com/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', adminView),
    path('admin/books', booksAdminView),
    path('admin/users', usersAdminView),
    path('api/', include('api.urls')),
    path('books/', listOfBooksView, name='listOfBooksView'),
    path('borrow/', listOfBorrowBooksView, name='borrow'),
    path('login/', loginView, name='login'),

]
