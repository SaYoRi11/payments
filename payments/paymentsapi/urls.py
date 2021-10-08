from django.urls import path, include
from .views import CardViewSet, InvoiceViewSet, PayByCardView, PayByGOFAAView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('card', CardViewSet, basename='card')
router.register('invoice', InvoiceViewSet, basename='invoice')

urlpatterns = [
    path('api/', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
    path('api/pay/user/', PayByGOFAAView.as_view()),
    path('api/pay/card/', PayByCardView.as_view())
]