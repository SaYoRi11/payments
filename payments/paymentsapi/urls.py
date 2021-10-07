from django.urls import path, include
from .views import CardViewSet, InvoiceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('card', CardViewSet, basename='card')
router.register('invoice', InvoiceViewSet, basename='invoice')

urlpatterns = [
    path('api/', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
]