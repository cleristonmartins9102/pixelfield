from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AccountViewSet, LoanViewSet
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'users', AccountViewSet)
router.register(r'register', AccountViewSet, basename='register')
router.register(r'loan', LoanViewSet, basename='loan')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenRefreshView.as_view(), name='token'),
    path('refresh/', TokenObtainPairView.as_view(), name='token_refresh'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair')
]